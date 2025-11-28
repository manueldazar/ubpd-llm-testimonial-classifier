"""
conftest.py
Shared pytest fixtures and configuration for UBPD classifier tests.
"""

import sys
import os
import pytest
from pathlib import Path

# Add src to path so we can import the modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src" / "ubpd_classifier"))


@pytest.fixture
def sample_ontology():
    """Provides a sample ontology structure matching the UBPD ontology."""
    return {
        "tipo_documento": {
            "TD0": "No testimonial",
            "TD1": "Testimonio de víctima directa",
            "TD2": "Testimonio de familiar o persona buscadora",
            "TD3": "Testimonio de exintegrante de grupo armado",
            "TD4": "Testimonio de tercero testigo",
        },
        "tipo_hecho": {
            "TH1": "Desaparición forzada",
            "TH2": "Homicidio",
            "TH3": "Desplazamiento forzado",
            "TH4": "Violencia sexual",
            "TH5": "Reclutamiento de menores",
            "TH6": "Tortura o tratos crueles",
            "TH7": "Otros hechos relevantes",
        },
        "periodo": {
            "PER0": "No identificado",
            "PER1": "1985-1990",
            "PER2": "1991-2000",
            "PER3": "2001-2010",
            "PER4": "2011-2016",
            "PER5": "2017-2025",
        },
        "actores": {
            "ACT0": "No aparece actor",
            "ACT1": "Fuerza Pública o agentes estatales",
            "ACT2": "Guerrillas",
            "ACT3": "Paramilitares / AUC",
            "ACT4": "Grupos posdesmovilización / BACRIM",
            "ACT5": "Actor no identificado",
        },
        "ruteo": {
            "RU0": "No aplica",
            "RU1": "Búsqueda e identificación",
            "RU2": "Esclarecimiento y patrones",
            "RU3": "Atención psicosocial",
            "RU4": "No prioritario",
        },
    }


@pytest.fixture
def sample_victim_testimony():
    """Sample testimony from a direct victim."""
    return """
    Yo, María García, cuento que en 1997, en San Carlos, Antioquia, hombres armados 
    de la guerrilla se llevaron a mi esposo Juan. Debimos salir hacia Medellín.
    """


@pytest.fixture
def sample_non_testimonial():
    """Sample non-testimonial document (administrative)."""
    return "Oficio 123 de 2020. Remito informe técnico."


@pytest.fixture
def sample_displacement_testimony():
    """Sample testimony involving displacement."""
    return """
    En 2004, fuimos desplazados de nuestro municipio en el Cauca por grupos armados.
    Perdimos todo y tuvimos que huir a Cali.
    """


@pytest.fixture
def sample_sexual_violence_testimony():
    """Sample testimony involving sexual violence."""
    return """
    En el año 2000, grupos paramilitares llegaron a nuestro corregimiento en Bolívar.
    Las mujeres fueron víctimas de violencia sexual.
    """


@pytest.fixture
def valid_classification_response():
    """Valid classification response from LLM."""
    return {
        "tipo_documento": "TD1",
        "tipo_hecho": ["TH1", "TH3"],
        "territorio": ["Antioquia"],
        "periodo": "PER2",
        "actores": ["ACT2"],
        "ruteo": "RU1",
        "highlights": ["1997, en San Carlos, Antioquia", "se llevaron a mi esposo"],
    }


@pytest.fixture
def invalid_classification_response():
    """Invalid classification response (needs fixing)."""
    return {
        "tipo_documento": "INVALID",
        "tipo_hecho": ["TH1", "INVALID_CODE"],
        "territorio": "string instead of list",
        "periodo": "INVALID",
        "actores": "not a list",
        "ruteo": "INVALID",
        "highlights": "not a list",
    }


@pytest.fixture
def td0_classification_response():
    """Classification response for TD0 (non-testimonial) which should force RU0."""
    return {
        "tipo_documento": "TD0",
        "tipo_hecho": [],
        "territorio": ["No identificado"],
        "periodo": "PER5",
        "actores": ["ACT0"],
        "ruteo": "RU3",  # Will be forced to RU0
        "highlights": [],
    }
