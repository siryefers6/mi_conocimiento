"""
Objetivo: Usar @patch para reemplazar función
Referencia: @patch()
Tipo: decorador
Nivel: basico
"""

from unittest.mock import patch, Mock

def conseguir_precio():
    # Función que obtendría precio de API
    return 100

def calcular_total(cantidad):
    precio = conseguir_precio()
    return cantidad * precio

@patch("__main__.conseguir_precio")
def test_con_patch(mock_precio):
    """Reemplazar función con patch"""
    mock_precio.return_value = 50
    
    resultado = calcular_total(2)
    assert resultado == 100  # 2 * 50
    mock_precio.assert_called_once()

"""output
test_con_patch PASSED
"""
