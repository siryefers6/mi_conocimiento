"""
Objetivo: combinar iterables en tuplas
Referencia: zip
Tipo: funcion
Nivel: basico
"""

# carga de datos
nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 22]

# transformación
combinados = list(zip(nombres, edades))

# resultado
print(combinados)

"""output
[('Ana', 25), ('Luis', 30), ('Pedro', 22)]
"""
