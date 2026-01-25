"""
Objetivo: usar condicional como guard clause (validación temprana)
Referencia: if
Tipo: keyword
Nivel: basico
"""

# imports
# no aplica

# carga de datos
numero = -5

# transformación
if numero < 0:
    print("Número inválido")
else:
    print(f"Número válido: {numero}")

"""output
Número inválido
"""
