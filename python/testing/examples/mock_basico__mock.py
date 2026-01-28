"""
Objetivo: Usar Mock básico
Referencia: unittest.mock.Mock
Tipo: clase
Nivel: basico
"""

from unittest.mock import Mock

def obtener_usuario_api(id):
    # Función que llamaría a una API
    pass

def test_con_mock():
    """Reemplazar función con mock"""
    mock_api = Mock(return_value={"id": 1, "nombre": "Ana"})
    
    resultado = mock_api(1)
    
    # Verificar que el mock fue llamado
    assert resultado == {"id": 1, "nombre": "Ana"}
    mock_api.assert_called_once_with(1)

def test_mock_multiples_llamadas():
    """Mock con múltiples llamadas"""
    mock = Mock()
    
    mock(1)
    mock(2)
    mock(3)
    
    # Verificar número de llamadas
    assert mock.call_count == 3

"""output
test_con_mock PASSED
test_mock_multiples_llamadas PASSED
"""
