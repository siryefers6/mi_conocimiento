"""
Objetivo: Acceder a información de excepción
Referencia: excinfo
Tipo: parámetro
Nivel: basico
"""

import pytest

def procesar_datos(datos):
    if not isinstance(datos, list):
        raise ValueError("datos debe ser lista")
    if len(datos) == 0:
        raise ValueError("datos no puede estar vacía")
    return sum(datos)

def test_acceder_info_excepcion():
    """Acceder a detalles de la excepción"""
    with pytest.raises(ValueError) as excinfo:
        procesar_datos("no es lista")
    
    # Verificar mensaje
    assert "debe ser lista" in str(excinfo.value)
    # Verificar tipo
    assert excinfo.type == ValueError

def test_excepcion_multiple():
    """Otro caso de excepción"""
    with pytest.raises(ValueError) as exc_info:
        procesar_datos([])
    
    assert "vacía" in str(exc_info.value)

"""output
test_acceder_info_excepcion PASSED
test_excepcion_multiple PASSED
"""
