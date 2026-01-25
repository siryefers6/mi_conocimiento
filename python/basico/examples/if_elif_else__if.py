"""
Objetivo: demostrar condicional con múltiples ramas
Referencia: if / elif / else
Tipo: keyword
Nivel: basico
"""

# imports
# no aplica

# carga de datos
nota = 7

# transformación
if nota >= 9:
    mensaje = "Sobresaliente"
elif nota >= 7:
    mensaje = "Aprobado"
else:
    mensaje = "Reprobado"

# resultado
print(mensaje)

"""output
Aprobado
"""
