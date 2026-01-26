"""
Objetivo: eliminar y retornar un par arbitrario
Referencia: dict.popitem
Tipo: metodo
Nivel: basico
"""

# carga de datos
usuario = {"nombre": "Ana", "edad": 30}

# transformación
par = usuario.popitem()  # elimina un par arbitrario (último agregado en Python 3.7+)

# resultado
print(usuario)
print(par)

"""output
{'nombre': 'Ana'}
('edad', 30)
"""
