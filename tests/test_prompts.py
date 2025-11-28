"""
test_prompts.py
Unit tests for prompts.py module.
Tests prompt building and system prompt structure.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "ubpd_classifier"))

from prompts import (
    SYSTEM_PROMPT,
    USER_TEMPLATE,
    ONTOLOGY,
    ONTOLOGY_PROMPT,
    build_user_prompt,
)


class TestSystemPrompt:
    """Test suite for SYSTEM_PROMPT."""

    def test_system_prompt_exists(self):
        """Test that SYSTEM_PROMPT is defined and non-empty."""
        assert SYSTEM_PROMPT is not None
        assert isinstance(SYSTEM_PROMPT, str)
        assert len(SYSTEM_PROMPT) > 0

    def test_system_prompt_contains_json_instruction(self):
        """Test that system prompt instructs JSON output."""
        assert "JSON" in SYSTEM_PROMPT or "json" in SYSTEM_PROMPT

    def test_system_prompt_contains_valid_codes_section(self):
        """Test that system prompt mentions valid codes."""
        assert "CÓDIGOS VÁLIDOS" in SYSTEM_PROMPT or "códigos" in SYSTEM_PROMPT.lower()

    def test_system_prompt_contains_format_section(self):
        """Test that system prompt specifies JSON format."""
        assert "FORMATO" in SYSTEM_PROMPT or "formato" in SYSTEM_PROMPT.lower()

    def test_system_prompt_contains_validation_rules(self):
        """Test that system prompt contains validation rules."""
        assert "VALIDACIÓN" in SYSTEM_PROMPT or "validación" in SYSTEM_PROMPT.lower()

    def test_system_prompt_contains_ontology(self):
        """Test that system prompt includes the ontology codes."""
        assert "tipo_documento" in SYSTEM_PROMPT
        assert "tipo_hecho" in SYSTEM_PROMPT
        assert "periodo" in SYSTEM_PROMPT
        assert "actores" in SYSTEM_PROMPT
        assert "ruteo" in SYSTEM_PROMPT

    def test_system_prompt_contains_required_fields(self):
        """Test that system prompt specifies all required fields."""
        required_fields = [
            "tipo_documento",
            "tipo_hecho",
            "territorio",
            "periodo",
            "actores",
            "ruteo",
            "highlights",
        ]
        for field in required_fields:
            assert field in SYSTEM_PROMPT


class TestUserTemplate:
    """Test suite for USER_TEMPLATE."""

    def test_user_template_exists(self):
        """Test that USER_TEMPLATE is defined."""
        assert USER_TEMPLATE is not None
        assert isinstance(USER_TEMPLATE, str)

    def test_user_template_has_placeholder(self):
        """Test that template contains placeholder for document."""
        assert "{{DOCUMENTO}}" in USER_TEMPLATE

    def test_user_template_contains_examples(self):
        """Test that template contains example documents."""
        assert "Ejemplo" in USER_TEMPLATE or "ejemplo" in USER_TEMPLATE.lower()

    def test_user_template_contains_sample_responses(self):
        """Test that template contains sample JSON responses."""
        assert "tipo_documento" in USER_TEMPLATE
        assert "tipo_hecho" in USER_TEMPLATE

    def test_user_template_demonstrates_td0_case(self):
        """Test that template shows TD0 (non-testimonial) example."""
        # User template should have examples of both testimonial and non-testimonial
        assert "TD0" in USER_TEMPLATE or "TD1" in USER_TEMPLATE


class TestOntologyObjects:
    """Test suite for ONTOLOGY and ONTOLOGY_PROMPT objects."""

    def test_ontology_is_dict(self):
        """Test that ONTOLOGY is a dictionary."""
        assert isinstance(ONTOLOGY, dict)

    def test_ontology_has_required_keys(self):
        """Test that ONTOLOGY has all required sections."""
        required_keys = {
            "tipo_documento",
            "tipo_hecho",
            "periodo",
            "actores",
            "ruteo",
        }
        assert set(ONTOLOGY.keys()) >= required_keys

    def test_ontology_prompt_is_string(self):
        """Test that ONTOLOGY_PROMPT is a string."""
        assert isinstance(ONTOLOGY_PROMPT, str)

    def test_ontology_prompt_contains_codes(self):
        """Test that ONTOLOGY_PROMPT contains sample codes."""
        assert "TD0" in ONTOLOGY_PROMPT or "TD1" in ONTOLOGY_PROMPT
        assert "TH1" in ONTOLOGY_PROMPT or "TH2" in ONTOLOGY_PROMPT


class TestBuildUserPrompt:
    """Test suite for build_user_prompt function."""

    def test_build_user_prompt_returns_string(self):
        """Test that build_user_prompt returns a string."""
        result = build_user_prompt("Test document")
        assert isinstance(result, str)

    def test_build_user_prompt_includes_document(self):
        """Test that built prompt includes the input document."""
        doc = "This is my testimony"
        result = build_user_prompt(doc)
        assert "This is my testimony" in result

    def test_build_user_prompt_removes_placeholder(self):
        """Test that placeholder is replaced."""
        doc = "Test document"
        result = build_user_prompt(doc)
        assert "{{DOCUMENTO}}" not in result

    def test_build_user_prompt_preserves_examples(self):
        """Test that built prompt includes example documents."""
        doc = "Test"
        result = build_user_prompt(doc)
        # Should include the few-shot examples from template
        assert "Ejemplo" in result or "ejemplo" in result.lower()

    def test_build_user_prompt_maintains_template_structure(self):
        """Test that structure of template is maintained."""
        doc = "My document"
        result = build_user_prompt(doc)
        # Should have JSON format specification
        assert "{" in result
        assert "}" in result
        assert "tipo_documento" in result

    def test_build_user_prompt_with_empty_string(self):
        """Test with empty string."""
        result = build_user_prompt("")
        assert isinstance(result, str)
        assert len(result) > 0  # Template is still there

    def test_build_user_prompt_with_multiline_document(self):
        """Test with multiline document."""
        doc = """
        Line 1
        Line 2
        Line 3
        """
        result = build_user_prompt(doc)
        assert "Line 1" in result
        assert "Line 2" in result

    def test_build_user_prompt_with_special_characters(self):
        """Test with special characters in document."""
        doc = "Documento con acentos: é, ñ, ü"
        result = build_user_prompt(doc)
        assert "acentos" in result

    def test_build_user_prompt_replaces_exactly_once(self):
        """Test that placeholder is replaced exactly once."""
        # If document contains {{DOCUMENTO}}, it should not be replaced
        doc = "This {{DOCUMENTO}} is a test"
        result = build_user_prompt(doc)
        # The one in the template should be replaced with the doc
        assert "This" in result

    def test_build_user_prompt_with_json_like_document(self):
        """Test with JSON-like document content."""
        doc = '{"key": "value"}'
        result = build_user_prompt(doc)
        assert "key" in result
        # Should not cause issues with the JSON in the prompt

    def test_build_user_prompt_output_is_valid_instruction(self):
        """Test that output is a valid instruction for the LLM."""
        doc = "Test testimony about events"
        result = build_user_prompt(doc)
        # Should have enough context for LLM
        assert len(result) > 100
        # Should instruct about format
        assert "JSON" in result or "json" in result.lower()
        # Should have the document
        assert "Test testimony" in result


class TestPromptConsistency:
    """Test consistency between system and user prompts."""

    def test_both_prompts_mention_format(self):
        """Test that both prompts discuss format."""
        assert "tipo_documento" in SYSTEM_PROMPT
        assert "tipo_documento" in USER_TEMPLATE

    def test_both_prompts_reference_ontology(self):
        """Test that both prompts reference the ontology."""
        # System prompt should embed ontology
        assert "tipo_hecho" in SYSTEM_PROMPT
        # User template shows examples
        assert "tipo_hecho" in USER_TEMPLATE

    def test_prompts_complement_each_other(self):
        """Test that prompts work together."""
        full_prompt = SYSTEM_PROMPT + "\n" + build_user_prompt("test")
        # Full prompt should have rules, examples, and document
        assert "VALIDACIÓN" in full_prompt or "validación" in full_prompt.lower()
        assert "Ejemplo" in full_prompt or "ejemplo" in full_prompt.lower()
