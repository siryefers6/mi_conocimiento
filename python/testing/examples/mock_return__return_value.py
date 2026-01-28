"""
Objetivo: Mock con return_value
Referencia: return_value=
Tipo: parámetro
Nivel: basico
"""

from unittest.mock import Mock

def test_mock_return_value():
    """Mock que retorna valor específico"""
    mock = Mock(return_value=42)
    
    resultado = mock()
    assert resultado == 42
    
    resultado2 = mock()
    assert resultado2 == 42

def test_mock_side_effect():
    """Mock con efecto secundario"""
    mock = Mock(side_effect=[1, 2, 3])
    
    assert mock() == 1
    assert mock() == 2
    assert mock() == 3

def test_mock_side_effect_exception():
    """Mock que lanza excepción"""
    mock = Mock(side_effect=ValueError("Error intencional"))
    
    import pytest
    with pytest.raises(ValueError):
        mock()

"""output
test_mock_return_value PASSED
test_mock_side_effect PASSED
test_mock_side_effect_exception PASSED
"""
