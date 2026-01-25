"""
Objetivo: manejar errores en tiempo de ejecución
Referencia: try / except
Tipo: keyword
Nivel: basico
"""

# imports
# no aplica

# carga de datos
texto = "abc"

# transformación
try:
    numero = int(texto)
except ValueError:
    numero = 0

# resultado
print(numero)

"""output
0
"""
