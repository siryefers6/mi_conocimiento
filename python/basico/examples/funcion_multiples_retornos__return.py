"""
Objetivo: Retornar múltiples valores usando tuplas
Referencia: return
Tipo: keyword
Nivel: basico
"""

# retornar múltiple
def obtener_datos():
    nombre = "Ana"
    edad = 30
    return nombre, edad

nombre, edad = obtener_datos()
print(f"{nombre}, {edad}")

# retornar diccionario
def get_persona():
    return {"nombre": "Juan", "edad": 25}

datos = get_persona()
print(datos)

# retornar lista
def numeros():
    return [1, 2, 3, 4, 5]

lista = numeros()
print(lista)

"""output
Ana, 30
{'nombre': 'Juan', 'edad': 25}
[1, 2, 3, 4, 5]
"""
