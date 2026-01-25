"""
Objetivo: condicional con múltiples condiciones usando and / or
Referencia: if
Tipo: keyword
Nivel: basico
"""

# imports
# no aplica

# carga de datos
edad = 20
tiene_identificacion = True

# transformación
if edad >= 18 and tiene_identificacion:
    mensaje = "Puede votar"
else:
    mensaje = "No puede votar"

# resultado
print(mensaje)

"""output
Puede votar
"""
