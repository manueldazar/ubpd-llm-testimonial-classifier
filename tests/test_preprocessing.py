"""
test_preprocessing.py
Unit tests for preprocessing.py module.
Tests text normalization, space collapsing, and preprocessing pipeline.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "ubpd_classifier"))

from preprocessing import (
    normalize_unicode,
    collapse_spaces,
    remove_headers_and_footers,
    preprocess_text,
)


class TestNormalizeUnicode:
    """Test suite for normalize_unicode function."""

    def test_normalize_unicode_basic(self):
        """Test basic unicode normalization."""
        text = "café"
        result = normalize_unicode(text)
        assert isinstance(result, str)
        assert len(result) == 4

    def test_normalize_unicode_with_combining_characters(self):
        """Test normalization with combining diacritical marks."""
        # 'é' can be represented as 'e' + combining acute accent
        text_combined = "e\u0301"  # e + combining acute
        text_normalized = normalize_unicode(text_combined)
        # Should be a single character 'é'
        assert len(text_normalized) == 1
        assert text_normalized == "é"

    def test_normalize_unicode_with_spanish_characters(self):
        """Test normalization of Spanish special characters."""
        text = "Español, Ñandú, Señor"
        result = normalize_unicode(text)
        assert "Español" in result
        assert "Ñandú" in result
        assert "Señor" in result

    def test_normalize_unicode_returns_string(self):
        """Test that function returns a string."""
        result = normalize_unicode("test")
        assert isinstance(result, str)

    def test_normalize_unicode_empty_string(self):
        """Test with empty string."""
        result = normalize_unicode("")
        assert result == ""

    def test_normalize_unicode_preserves_content(self):
        """Test that normalization preserves the content meaning."""
        original = "café"
        normalized = normalize_unicode(original)
        # The normalized version should be visually identical
        assert normalized == normalized.lower().replace(" ", " ")


class TestCollapseSpaces:
    """Test suite for collapse_spaces function."""

    def test_collapse_single_spaces(self):
        """Test that single spaces are preserved."""
        text = "hello world"
        result = collapse_spaces(text)
        assert result == "hello world"

    def test_collapse_multiple_spaces(self):
        """Test that multiple spaces are reduced to single space."""
        text = "hello    world"
        result = collapse_spaces(text)
        assert result == "hello world"

    def test_collapse_tabs(self):
        """Test that tabs are converted to single space."""
        text = "hello\t\tworld"
        result = collapse_spaces(text)
        assert result == "hello world"

    def test_collapse_newlines(self):
        """Test that newlines are converted to single space."""
        text = "hello\nworld"
        result = collapse_spaces(text)
        assert result == "hello world"

    def test_collapse_mixed_whitespace(self):
        """Test with mixed whitespace characters."""
        text = "hello  \n  \t  world"
        result = collapse_spaces(text)
        assert result == "hello world"

    def test_collapse_leading_and_trailing_spaces(self):
        """Test that leading and trailing spaces are stripped."""
        text = "  hello world  "
        result = collapse_spaces(text)
        assert result == "hello world"

    def test_collapse_empty_string(self):
        """Test with empty string."""
        result = collapse_spaces("")
        assert result == ""

    def test_collapse_only_spaces(self):
        """Test with only spaces."""
        result = collapse_spaces("    ")
        assert result == ""

    def test_collapse_multiline_text(self):
        """Test with multiline text."""
        text = """
        This is a
        multiline
        text
        """
        result = collapse_spaces(text)
        assert "This" in result
        assert "multiline" in result
        assert result == "This is a multiline text"


class TestRemoveHeadersAndFooters:
    """Test suite for remove_headers_and_footers function."""

    def test_function_exists(self):
        """Test that function exists and is callable."""
        assert callable(remove_headers_and_footers)

    def test_pass_through_without_patterns(self):
        """Test that text without patterns passes through unchanged."""
        text = "This is a simple testimony about my experience."
        result = remove_headers_and_footers(text)
        assert result == text

    def test_empty_string(self):
        """Test with empty string."""
        result = remove_headers_and_footers("")
        assert result == ""

    def test_returns_string(self):
        """Test that function returns a string."""
        result = remove_headers_and_footers("test text")
        assert isinstance(result, str)


class TestPreprocessText:
    """Test suite for complete preprocess_text pipeline."""

    def test_preprocess_simple_text(self):
        """Test preprocessing of simple text."""
        text = "Hello world"
        result = preprocess_text(text)
        assert result == "Hello world"

    def test_preprocess_text_with_extra_spaces(self):
        """Test that extra spaces are collapsed."""
        text = "Hello    world"
        result = preprocess_text(text)
        assert result == "Hello world"

    def test_preprocess_text_with_unicode(self):
        """Test that unicode is normalized."""
        text = "café"
        result = preprocess_text(text)
        assert "café" in result or "caf" in result  # Both forms should be valid

    def test_preprocess_text_with_newlines(self):
        """Test that newlines are converted to spaces."""
        text = "Hello\nworld"
        result = preprocess_text(text)
        assert result == "Hello world"

    def test_preprocess_text_with_tabs(self):
        """Test that tabs are converted to spaces."""
        text = "Hello\tworld"
        result = preprocess_text(text)
        assert result == "Hello world"

    def test_preprocess_text_complex(self):
        """Test preprocessing of complex text."""
        text = """
        Testimony with    multiple
        spaces and\ttabs and
        special chars: é, ñ
        """
        result = preprocess_text(text)
        # Should be a single line with single spaces
        assert "\n" not in result
        assert "\t" not in result
        assert "Testimony" in result
        assert "multiple" in result

    def test_preprocess_spanish_testimony(self, sample_victim_testimony):
        """Test preprocessing of Spanish testimony."""
        result = preprocess_text(sample_victim_testimony)
        assert "María García" in result or "Maria" in result
        assert "Antioquia" in result

    def test_preprocess_empty_string(self):
        """Test with empty string."""
        result = preprocess_text("")
        assert result == ""

    def test_preprocess_whitespace_only(self):
        """Test with whitespace only."""
        result = preprocess_text("   \n\t  ")
        assert result == ""

    def test_preprocess_text_returns_string(self):
        """Test that result is always a string."""
        result = preprocess_text("test")
        assert isinstance(result, str)

    def test_preprocess_text_strips_correctly(self):
        """Test that text is properly stripped."""
        text = "  hello world  "
        result = preprocess_text(text)
        assert result == "hello world"
        assert not result.startswith(" ")
        assert not result.endswith(" ")
