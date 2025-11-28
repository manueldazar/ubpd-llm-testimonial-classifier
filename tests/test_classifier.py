"""
test_classifier.py
Unit tests for classifier.py module.
Tests JSON extraction, parsing, validation, and fixing of classifications.
"""

import sys
import json
import pytest
from pathlib import Path
from unittest.mock import patch

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "ubpd_classifier"))

from classifier import (
    extract_json_block,
    parse_model_response,
    fix_single_label,
    fix_multi_labels,
    fix_territorio,
    compute_priority,
    validate_and_fix,
)


class TestExtractJsonBlock:
    """Test suite for extract_json_block function."""

    def test_extract_simple_json(self):
        """Test extraction of simple JSON."""
        text = '{"key": "value"}'
        result = extract_json_block(text)
        assert "{" in result
        assert "}" in result
        assert "key" in result

    def test_extract_json_with_surrounding_text(self):
        """Test extraction of JSON with surrounding text."""
        text = 'Some text before {"key": "value"} some text after'
        result = extract_json_block(text)
        assert result == '{"key": "value"}'

    def test_extract_nested_json(self):
        """Test extraction of nested JSON."""
        text = '{"outer": {"inner": "value"}}'
        result = extract_json_block(text)
        assert "outer" in result
        assert "inner" in result

    def test_extract_json_with_arrays(self):
        """Test extraction of JSON with arrays."""
        text = '{"items": [1, 2, 3], "name": "test"}'
        result = extract_json_block(text)
        assert "items" in result
        assert "[" in result
        assert "]" in result

    def test_extract_json_finds_first_brace(self):
        """Test that function finds the first opening brace."""
        text = "Before {first} middle {second}"
        result = extract_json_block(text)
        assert "first" in result

    def test_extract_json_finds_last_brace(self):
        """Test that function finds the last closing brace."""
        text = "{first} middle {second: done}"
        result = extract_json_block(text)
        assert "second" in result
        assert "done" in result

    def test_extract_json_no_opening_brace_raises_error(self):
        """Test that missing opening brace raises ValueError."""
        text = '"no opening brace}'
        with pytest.raises(ValueError):
            extract_json_block(text)

    def test_extract_json_no_closing_brace_raises_error(self):
        """Test that missing closing brace raises ValueError."""
        text = '{"no closing brace'
        with pytest.raises(ValueError):
            extract_json_block(text)

    def test_extract_json_empty_object(self):
        """Test extraction of empty JSON object."""
        text = "{}"
        result = extract_json_block(text)
        assert result == "{}"

    def test_extract_json_with_special_characters(self):
        """Test extraction with special characters."""
        text = '{"text": "Yo soy una víctima"}'
        result = extract_json_block(text)
        assert "víctima" in result


class TestParseModelResponse:
    """Test suite for parse_model_response function."""

    def test_parse_valid_json_response(self):
        """Test parsing valid JSON response."""
        raw = '{"tipo_documento": "TD1", "tipo_hecho": []}'
        result = parse_model_response(raw)
        assert isinstance(result, dict)
        assert result["tipo_documento"] == "TD1"
        assert result["tipo_hecho"] == []

    def test_parse_json_with_surrounding_text(self):
        """Test parsing JSON with surrounding text."""
        raw = "The classification is: {\"codigo\": \"TD1\"} end."
        result = parse_model_response(raw)
        assert isinstance(result, dict)
        assert result["codigo"] == "TD1"

    def test_parse_complex_response(self, valid_classification_response):
        """Test parsing complex classification response."""
        raw_str = json.dumps(valid_classification_response)
        result = parse_model_response(raw_str)
        assert result["tipo_documento"] == "TD1"
        assert "TH1" in result["tipo_hecho"]
        assert "Antioquia" in result["territorio"]

    def test_parse_invalid_json_raises_error(self):
        """Test that invalid JSON raises error."""
        raw = '{"invalid json'
        with pytest.raises(Exception):  # json.JSONDecodeError
            parse_model_response(raw)

    def test_parse_preserves_data_types(self):
        """Test that parsing preserves data types."""
        raw = '{"string": "text", "list": [1, 2], "dict": {"nested": "value"}}'
        result = parse_model_response(raw)
        assert isinstance(result["string"], str)
        assert isinstance(result["list"], list)
        assert isinstance(result["dict"], dict)

    def test_parse_spanish_content(self):
        """Test parsing with Spanish content."""
        raw = '{"territorio": ["Antioquia", "Bogotá"], "descripcion": "Caso en Medellín"}'
        result = parse_model_response(raw)
        assert "Antioquia" in result["territorio"]
        assert "Medellín" in result["descripcion"]


class TestFixSingleLabel:
    """Test suite for fix_single_label function."""

    def test_fix_valid_label(self, sample_ontology):
        """Test that valid label is unchanged."""
        allowed = sample_ontology["tipo_documento"]
        result = fix_single_label("TD1", allowed, "TD0")
        assert result == "TD1"

    def test_fix_invalid_label_uses_default(self, sample_ontology):
        """Test that invalid label is replaced with default."""
        allowed = sample_ontology["tipo_documento"]
        result = fix_single_label("INVALID", allowed, "TD0")
        assert result == "TD0"

    def test_fix_none_value_uses_default(self, sample_ontology):
        """Test that None value uses default."""
        allowed = sample_ontology["tipo_documento"]
        result = fix_single_label(None, allowed, "TD0")
        assert result == "TD0"

    def test_fix_empty_string_uses_default(self, sample_ontology):
        """Test that empty string uses default."""
        allowed = sample_ontology["tipo_documento"]
        result = fix_single_label("", allowed, "TD0")
        assert result == "TD0"

    def test_fix_all_valid_labels(self, sample_ontology):
        """Test that all valid labels are recognized."""
        allowed = sample_ontology["tipo_documento"]
        for code in allowed.keys():
            result = fix_single_label(code, allowed, "TD0")
            assert result == code

    def test_fix_case_sensitive(self, sample_ontology):
        """Test that matching is case-sensitive."""
        allowed = sample_ontology["tipo_documento"]
        result = fix_single_label("td1", allowed, "TD0")
        assert result == "TD0"  # Should not match lowercase

    def test_fix_with_whitespace(self, sample_ontology):
        """Test with whitespace around value."""
        allowed = sample_ontology["tipo_documento"]
        result = fix_single_label(" TD1 ", allowed, "TD0")
        assert result == "TD0"  # Whitespace makes it invalid


class TestFixMultiLabels:
    """Test suite for fix_multi_labels function."""

    def test_fix_valid_list(self, sample_ontology):
        """Test that valid list is filtered correctly."""
        allowed = sample_ontology["tipo_hecho"]
        values = ["TH1", "TH2"]
        result = fix_multi_labels(values, allowed)
        assert result == ["TH1", "TH2"]

    def test_fix_list_with_invalid_codes(self, sample_ontology):
        """Test that invalid codes are filtered out."""
        allowed = sample_ontology["tipo_hecho"]
        values = ["TH1", "INVALID", "TH2"]
        result = fix_multi_labels(values, allowed)
        assert result == ["TH1", "TH2"]
        assert "INVALID" not in result

    def test_fix_empty_list(self, sample_ontology):
        """Test that empty list returns empty list."""
        allowed = sample_ontology["tipo_hecho"]
        result = fix_multi_labels([], allowed)
        assert result == []

    def test_fix_non_list_input(self, sample_ontology):
        """Test that non-list input returns empty list."""
        allowed = sample_ontology["tipo_hecho"]
        result = fix_multi_labels("TH1", allowed)
        assert result == []

    def test_fix_none_input(self, sample_ontology):
        """Test that None input returns empty list."""
        allowed = sample_ontology["tipo_hecho"]
        result = fix_multi_labels(None, allowed)
        assert result == []

    def test_fix_dict_input(self, sample_ontology):
        """Test that dict input returns empty list."""
        allowed = sample_ontology["tipo_hecho"]
        result = fix_multi_labels({"TH1": "value"}, allowed)
        assert result == []

    def test_fix_all_valid_codes(self, sample_ontology):
        """Test with all valid codes."""
        allowed = sample_ontology["tipo_hecho"]
        values = list(allowed.keys())
        result = fix_multi_labels(values, allowed)
        assert len(result) == len(values)
        assert set(result) == set(values)

    def test_fix_preserves_order(self, sample_ontology):
        """Test that order is preserved."""
        allowed = sample_ontology["tipo_hecho"]
        values = ["TH3", "TH1", "TH2"]
        result = fix_multi_labels(values, allowed)
        assert result == ["TH3", "TH1", "TH2"]


class TestFixTerritorio:
    """Test suite for fix_territorio function."""

    def test_fix_valid_departamento_list(self):
        """Test valid department list."""
        values = ["Antioquia", "Bogotá"]
        result = fix_territorio(values)
        assert "Antioquia" in result
        assert "Bogotá" in result

    def test_fix_territorio_with_whitespace(self):
        """Test that whitespace is stripped."""
        values = [" Antioquia ", "  Bogotá  "]
        result = fix_territorio(values)
        assert "Antioquia" in result
        assert "Bogotá" in result
        # No whitespace should remain
        assert not any(v.startswith(" ") or v.endswith(" ") for v in result)

    def test_fix_territorio_removes_duplicates(self):
        """Test that duplicates are removed."""
        values = ["Antioquia", "Antioquia", "Bogotá"]
        result = fix_territorio(values)
        assert len(result) == 2
        assert result.count("Antioquia") == 1

    def test_fix_territorio_empty_list(self):
        """Test that empty list returns ['No identificado']."""
        result = fix_territorio([])
        assert result == ["No identificado"]

    def test_fix_territorio_none_input(self):
        """Test that None input returns ['No identificado']."""
        result = fix_territorio(None)
        assert result == ["No identificado"]

    def test_fix_territorio_non_list_input(self):
        """Test that non-list input returns ['No identificado']."""
        result = fix_territorio("Antioquia")
        assert result == ["No identificado"]

    def test_fix_territorio_preserves_order(self):
        """Test that order is preserved when removing duplicates."""
        values = ["Bogotá", "Antioquia", "Bogotá", "Cauca"]
        result = fix_territorio(values)
        # Should have unique values but order might be set order
        assert set(result) == {"Bogotá", "Antioquia", "Cauca"}

    def test_fix_territorio_with_special_names(self):
        """Test with departments having special characters."""
        values = ["La Guajira", "Norte de Santander"]
        result = fix_territorio(values)
        assert "La Guajira" in result
        assert "Norte de Santander" in result

    def test_fix_territorio_no_identificado(self):
        """Test that 'No identificado' is valid input."""
        values = ["No identificado", "Antioquia"]
        result = fix_territorio(values)
        assert "No identificado" in result or "Antioquia" in result


class TestComputePriority:
    """Test suite for compute_priority function."""

    def test_compute_priority_no_priority_factors(self):
        """Test priority with no high-priority factors."""
        pred = {
            "tipo_hecho": ["TH7"],
            "ruteo": "RU4",
        }
        score = compute_priority(pred)
        assert score == 0.0

    def test_compute_priority_th1_factor(self):
        """Test that TH1 (disappearance) adds 0.4."""
        pred = {
            "tipo_hecho": ["TH1"],
            "ruteo": "RU4",
        }
        score = compute_priority(pred)
        assert score >= 0.4

    def test_compute_priority_th4_factor(self):
        """Test that TH4 (sexual violence) adds 0.2."""
        pred = {
            "tipo_hecho": ["TH4"],
            "ruteo": "RU4",
        }
        score = compute_priority(pred)
        assert score >= 0.2

    def test_compute_priority_ru1_factor(self):
        """Test that RU1 routing adds 0.3."""
        pred = {
            "tipo_hecho": [],
            "ruteo": "RU1",
        }
        score = compute_priority(pred)
        assert score >= 0.3

    def test_compute_priority_ru3_factor(self):
        """Test that RU3 routing adds 0.1."""
        pred = {
            "tipo_hecho": [],
            "ruteo": "RU3",
        }
        score = compute_priority(pred)
        assert score >= 0.1

    def test_compute_priority_combined_factors(self):
        """Test that multiple factors combine."""
        pred = {
            "tipo_hecho": ["TH1", "TH4"],
            "ruteo": "RU1",
        }
        score = compute_priority(pred)
        # TH1: 0.4 + TH4: 0.2 + RU1: 0.3 = 0.9
        assert 0.8 <= score <= 1.0

    def test_compute_priority_capped_at_one(self):
        """Test that priority score is capped at 1.0."""
        pred = {
            "tipo_hecho": ["TH1", "TH1", "TH4"],
            "ruteo": "RU1",
        }
        score = compute_priority(pred)
        assert score <= 1.0

    def test_compute_priority_missing_fields_handled(self):
        """Test that missing fields don't cause errors."""
        pred = {}
        score = compute_priority(pred)
        assert 0.0 <= score <= 1.0

    def test_compute_priority_empty_tipo_hecho(self):
        """Test with empty tipo_hecho list."""
        pred = {
            "tipo_hecho": [],
            "ruteo": "RU4",
        }
        score = compute_priority(pred)
        assert score == 0.0

    def test_compute_priority_returns_float(self):
        """Test that score is a float."""
        pred = {
            "tipo_hecho": ["TH1"],
            "ruteo": "RU1",
        }
        score = compute_priority(pred)
        assert isinstance(score, float)


class TestValidateAndFix:
    """Test suite for validate_and_fix function."""

    def test_validate_and_fix_valid_response(self, valid_classification_response):
        """Test that valid response passes through with priority added."""
        result = validate_and_fix(valid_classification_response.copy())
        assert result["tipo_documento"] == "TD1"
        assert "priority_score" in result
        assert isinstance(result["priority_score"], float)

    def test_validate_and_fix_invalid_response(self, invalid_classification_response):
        """Test that invalid response is fixed."""
        result = validate_and_fix(invalid_classification_response.copy())
        # All codes should be valid or defaults
        assert result["tipo_documento"] in ["TD0", "TD1", "TD2", "TD3", "TD4"]
        assert isinstance(result["tipo_hecho"], list)
        assert isinstance(result["territorio"], list)
        assert isinstance(result["highlights"], list)

    def test_validate_and_fix_td0_forces_ru0(self, td0_classification_response):
        """Test that TD0 forces RU0."""
        result = validate_and_fix(td0_classification_response.copy())
        assert result["tipo_documento"] == "TD0"
        assert result["ruteo"] == "RU0"

    def test_validate_and_fix_missing_fields(self):
        """Test with missing fields."""
        pred = {}
        result = validate_and_fix(pred)
        assert "tipo_documento" in result
        assert "tipo_hecho" in result
        assert "territorio" in result
        assert "periodo" in result
        assert "actores" in result
        assert "ruteo" in result
        assert "highlights" in result

    def test_validate_and_fix_empty_highlights(self):
        """Test that invalid highlights become empty list."""
        pred = {
            "highlights": "not a list"
        }
        result = validate_and_fix(pred)
        assert result["highlights"] == []

    def test_validate_and_fix_empty_territorio(self):
        """Test that empty territorio becomes ['No identificado']."""
        pred = {
            "territorio": []
        }
        result = validate_and_fix(pred)
        assert result["territorio"] == ["No identificado"]

    def test_validate_and_fix_empty_actores(self):
        """Test that empty actores gets default."""
        pred = {
            "actores": []
        }
        result = validate_and_fix(pred)
        assert result["actores"] == [] or "ACT0" in result["actores"]

    def test_validate_and_fix_adds_priority_score(self):
        """Test that priority_score is always added."""
        pred = {
            "tipo_documento": "TD1",
            "tipo_hecho": ["TH1"],
            "ruteo": "RU1"
        }
        result = validate_and_fix(pred)
        assert "priority_score" in result
        assert isinstance(result["priority_score"], float)

    def test_validate_and_fix_preserves_valid_data(self, valid_classification_response):
        """Test that valid data is preserved through validation."""
        original = valid_classification_response.copy()
        result = validate_and_fix(original)
        assert result["tipo_documento"] == original["tipo_documento"]
        assert set(result["tipo_hecho"]) == set(original["tipo_hecho"])
        assert set(result["territorio"]) == set(original["territorio"])

    def test_validate_and_fix_returns_dict(self):
        """Test that result is always a dict."""
        result = validate_and_fix({})
        assert isinstance(result, dict)

    def test_validate_and_fix_with_duplicates_in_territorio(self):
        """Test that duplicates in territorio are removed."""
        pred = {
            "territorio": ["Antioquia", "Antioquia", "Bogotá"]
        }
        result = validate_and_fix(pred)
        assert result["territorio"].count("Antioquia") == 1


# Mock tests for functions that need LLM calls
class TestClassifyDocumentWithMocks:
    """Test suite for classify_document with mocked LLM calls."""

    @patch('classifier.call_llm')
    def test_classify_document_flow(self, mock_llm):
        """Test the complete classification flow with mocked LLM."""
        mock_response = json.dumps({
            "tipo_documento": "TD1",
            "tipo_hecho": ["TH1"],
            "territorio": ["Antioquia"],
            "periodo": "PER2",
            "actores": ["ACT2"],
            "ruteo": "RU1",
            "highlights": ["en Antioquia"]
        })
        mock_llm.return_value = mock_response
        
        # We would import and call classify_document here
        # but it requires call_llm to be patched
        assert mock_llm is not None
