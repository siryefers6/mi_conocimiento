"""
Objetivo: Test que verifica excepciones
Referencia: pytest.raises()
Tipo: función
Nivel: basico
"""

import pytest

def obtener_elemento(lista, indice):
    if indice < 0:
        raise ValueError("Índice no puede ser negativo")
    return lista[indice]

def test_indice_negativo_lanza_error():
    """Verificar que se lanza ValueError"""
    with pytest.raises(ValueError):
        obtener_elemento([1, 2, 3], -1)

def test_indice_fuera_de_rango():
    """Verificar IndexError"""
    with pytest.raises(IndexError):
        obtener_elemento([1, 2, 3], 100)

"""output
test_indice_negativo_lanza_error PASSED
test_indice_fuera_de_rango PASSED
"""
