"""
Objetivo: Assert para verificar None
Referencia: assert x is None
Tipo: operador
Nivel: basico
"""

def buscar_usuario(id):
    usuarios = {1: "Ana", 2: "Juan"}
    return usuarios.get(id)

def test_usuario_existe():
    """Usuario encontrado (no es None)"""
    assert buscar_usuario(1) is not None

def test_usuario_no_existe():
    """Usuario no encontrado (es None)"""
    assert buscar_usuario(999) is None

def test_valor_none_es_none():
    valor = None
    assert valor is None

"""output
test_usuario_existe PASSED
test_usuario_no_existe PASSED
test_valor_none_es_none PASSED
"""
