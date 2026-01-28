"""
Objetivo: Usar assert con mensajes personalizados
Referencia: assert ... , "mensaje"
Tipo: keyword
Nivel: basico
"""

def dividir(a, b):
    if b == 0:
        raise ValueError("División por cero")
    return a / b

def test_division_valida():
    """Test de división normal"""
    resultado = dividir(10, 2)
    assert resultado == 5.0, f"Esperaba 5.0, obtuve {resultado}"

def test_mensaje_descriptivo():
    """Test con mensaje claro"""
    numero = 5
    assert numero > 0, f"{numero} debe ser positivo"

"""output
test_division_valida PASSED
test_mensaje_descriptivo PASSED
"""
