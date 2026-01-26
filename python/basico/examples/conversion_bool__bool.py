"""
Objetivo: convertir distintos valores a booleano
Referencia: bool
Tipo: funcion
Nivel: basico
"""

# carga de datos
valores = [0, 1, "", "Hola", [], [1,2]]

# transformación
resultado = [bool(v) for v in valores]

# resultado
print(resultado)

"""output
[False, True, False, True, False, True]
"""
