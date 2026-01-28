"""
Objetivo: Redondear un número
Referencia: round
Tipo: función
Nivel: basico
"""

# redondear simple
numero = 3.7
redondeado = round(numero)
print(f"round(3.7) = {redondeado}")

# redondear a decimales
pi = 3.14159
redondeado2 = round(pi, 2)
print(f"round(3.14159, 2) = {redondeado2}")

# redondear hacia abajo
numero2 = 2.5
print(f"round(2.5) = {round(numero2)}")

"""output
round(3.7) = 4
round(3.14159, 2) = 3.14
round(2.5) = 2
"""
