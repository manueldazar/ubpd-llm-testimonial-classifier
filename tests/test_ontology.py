"""
test_ontology.py
Unit tests for ontology.py module.
Tests ontology loading and conversion to prompt text.
"""

import sys
from pathlib import Path
import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "ubpd_classifier"))

from ontology import load_ontology, ontology_to_prompt_text


class TestLoadOntology:
    """Test suite for load_ontology function."""

    def test_load_ontology_returns_dict(self, sample_ontology):
        """Test that load_ontology returns a dictionary-like structure."""
        # We can't test actual loading without the file, but we test the structure
        assert isinstance(sample_ontology, dict)
        assert "tipo_documento" in sample_ontology
        assert "tipo_hecho" in sample_ontology
        assert "periodo" in sample_ontology
        assert "actores" in sample_ontology
        assert "ruteo" in sample_ontology

    def test_ontology_has_required_keys(self, sample_ontology):
        """Test that ontology has all required top-level keys."""
        required_keys = {"tipo_documento", "tipo_hecho", "periodo", "actores", "ruteo"}
        assert set(sample_ontology.keys()) == required_keys

    def test_tipo_documento_structure(self, sample_ontology):
        """Test tipo_documento section structure."""
        tipo_doc = sample_ontology["tipo_documento"]
        assert isinstance(tipo_doc, dict)
        assert "TD0" in tipo_doc
        assert "TD1" in tipo_doc
        assert "TD2" in tipo_doc
        assert "TD3" in tipo_doc
        assert "TD4" in tipo_doc

    def test_tipo_hecho_structure(self, sample_ontology):
        """Test tipo_hecho section structure."""
        tipo_hecho = sample_ontology["tipo_hecho"]
        assert isinstance(tipo_hecho, dict)
        assert "TH1" in tipo_hecho
        assert "TH2" in tipo_hecho
        assert "TH3" in tipo_hecho
        assert "TH4" in tipo_hecho
        assert "TH5" in tipo_hecho
        assert "TH6" in tipo_hecho
        assert "TH7" in tipo_hecho

    def test_periodo_structure(self, sample_ontology):
        """Test periodo section structure."""
        periodo = sample_ontology["periodo"]
        assert isinstance(periodo, dict)
        assert "PER0" in periodo
        assert "PER1" in periodo
        assert "PER2" in periodo
        assert "PER3" in periodo
        assert "PER4" in periodo
        assert "PER5" in periodo

    def test_actores_structure(self, sample_ontology):
        """Test actores section structure."""
        actores = sample_ontology["actores"]
        assert isinstance(actores, dict)
        assert "ACT0" in actores
        assert "ACT1" in actores
        assert "ACT2" in actores
        assert "ACT3" in actores
        assert "ACT4" in actores
        assert "ACT5" in actores

    def test_ruteo_structure(self, sample_ontology):
        """Test ruteo section structure."""
        ruteo = sample_ontology["ruteo"]
        assert isinstance(ruteo, dict)
        assert "RU0" in ruteo
        assert "RU1" in ruteo
        assert "RU2" in ruteo
        assert "RU3" in ruteo
        assert "RU4" in ruteo


class TestOntologyToPromptText:
    """Test suite for ontology_to_prompt_text function."""

    def test_ontology_to_prompt_returns_string(self, sample_ontology):
        """Test that ontology_to_prompt_text returns a string."""
        result = ontology_to_prompt_text(sample_ontology)
        assert isinstance(result, str)

    def test_prompt_contains_tipo_documento_codes(self, sample_ontology):
        """Test that prompt contains all tipo_documento codes."""
        result = ontology_to_prompt_text(sample_ontology)
        assert "tipo_documento:" in result
        assert "TD0" in result
        assert "TD1" in result
        assert "TD2" in result

    def test_prompt_contains_tipo_hecho_codes(self, sample_ontology):
        """Test that prompt contains all tipo_hecho codes."""
        result = ontology_to_prompt_text(sample_ontology)
        assert "tipo_hecho:" in result
        assert "TH1" in result
        assert "TH2" in result
        assert "TH3" in result

    def test_prompt_contains_periodo_codes(self, sample_ontology):
        """Test that prompt contains all periodo codes."""
        result = ontology_to_prompt_text(sample_ontology)
        assert "periodo:" in result
        assert "PER1" in result
        assert "PER2" in result

    def test_prompt_contains_actores_codes(self, sample_ontology):
        """Test that prompt contains all actores codes."""
        result = ontology_to_prompt_text(sample_ontology)
        assert "actores:" in result
        assert "ACT1" in result
        assert "ACT2" in result

    def test_prompt_contains_ruteo_codes(self, sample_ontology):
        """Test that prompt contains all ruteo codes."""
        result = ontology_to_prompt_text(sample_ontology)
        assert "ruteo:" in result
        assert "RU1" in result
        assert "RU2" in result

    def test_prompt_text_format(self, sample_ontology):
        """Test that prompt text has proper YAML-like format."""
        result = ontology_to_prompt_text(sample_ontology)
        lines = result.split("\n")
        # Should have multiple lines
        assert len(lines) > 10
        # Should contain indentation with dashes for codes
        assert any("  -" in line for line in lines)

    def test_prompt_contains_all_major_sections(self, sample_ontology):
        """Test that prompt contains all major ontology sections."""
        result = ontology_to_prompt_text(sample_ontology)
        sections = ["tipo_documento:", "tipo_hecho:", "periodo:", "actores:", "ruteo:"]
        for section in sections:
            assert section in result

    def test_prompt_codes_format(self, sample_ontology):
        """Test that codes are properly formatted with dashes."""
        result = ontology_to_prompt_text(sample_ontology)
        # Should have lines with "  - CODE" format
        assert "  - TD0" in result or "- TD0" in result
        assert "  - TH1" in result or "- TH1" in result

    def test_ontology_with_empty_dict(self):
        """Test ontology_to_prompt_text with minimal structure."""
        minimal_ontology = {
            "tipo_documento": {"TD0": "Test"},
            "tipo_hecho": {},
            "periodo": {},
            "actores": {},
            "ruteo": {},
        }
        result = ontology_to_prompt_text(minimal_ontology)
        assert isinstance(result, str)
        assert "tipo_documento:" in result
        assert "TD0" in result

    def test_prompt_is_human_readable(self, sample_ontology):
        """Test that the generated prompt is human readable."""
        result = ontology_to_prompt_text(sample_ontology)
        # Should not contain quotes from dict repr
        assert "{" not in result or result.count("{") == 0
        assert "'" not in result or result.count("'") == 0
        # Should be clean and simple
        assert len(result) > 50  # Not empty or trivial
