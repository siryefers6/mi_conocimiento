"""
Objetivo: Assert para verificar contenido
Referencia: in, assert x in y
Tipo: operador
Nivel: basico
"""

def test_string_contiene():
    """Verificar substring"""
    mensaje = "Hola mundo"
    assert "mundo" in mensaje
    assert "Hola" in mensaje

def test_lista_contiene():
    """Verificar elemento en lista"""
    numeros = [1, 2, 3, 4, 5]
    assert 3 in numeros
    assert 10 not in numeros

def test_dict_contiene_clave():
    """Verificar clave en diccionario"""
    usuario = {"nombre": "Ana", "edad": 30}
    assert "nombre" in usuario
    assert "email" not in usuario

def test_dict_contiene_valor():
    """Verificar valor en diccionario"""
    datos = {"a": 1, "b": 2, "c": 3}
    assert 2 in datos.values()
    assert 10 not in datos.values()

"""output
test_string_contiene PASSED
test_lista_contiene PASSED
test_dict_contiene_clave PASSED
test_dict_contiene_valor PASSED
"""
