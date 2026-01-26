"""
Objetivo: obtener valor de clave o asignar si no existe
Referencia: dict.setdefault
Tipo: metodo
Nivel: basico
"""

# carga de datos
usuario = {"nombre": "Ana"}

# transformación
edad = usuario.setdefault("edad", 30)  # asigna 30 si no existe
nombre = usuario.setdefault("nombre", "Desconocido")  # no cambia nombre existente

# resultado
print(usuario)
print(edad)
print(nombre)

"""output
{'nombre': 'Ana', 'edad': 30}
30
Ana
"""
