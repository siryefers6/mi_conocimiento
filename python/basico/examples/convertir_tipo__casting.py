"""
Objetivo: convertir explícitamente el tipo de una variable
Referencia: int / str / float
Tipo: funcion
Nivel: basico
"""

# imports
# no aplica

# carga de datos
texto_numero = "42"
numero_decimal = 3.14

# transformación
entero = int(texto_numero)
texto = str(numero_decimal)
decimal = float(entero)

# resultado
print(entero)
print(texto)
print(decimal)

"""output
42
3.14
42.0
"""
