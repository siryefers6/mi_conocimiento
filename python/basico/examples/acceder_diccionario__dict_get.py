"""
Objetivo: acceder de forma segura a un diccionario
Referencia: dict.get
Tipo: metodo
Nivel: basico
"""

# imports
# no aplica

# carga de datos
usuario = {
    "nombre": "Ana",
    "edad": 30
}

# transformación
nombre = usuario.get("nombre")
ciudad = usuario.get("ciudad")  # clave inexistente

# resultado
print(nombre)
print(ciudad)

"""output
Ana
None
"""
