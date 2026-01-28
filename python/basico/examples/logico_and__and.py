"""
Objetivo: Evaluar si ambas condiciones son verdaderas
Referencia: and
Tipo: operador
Nivel: basico
"""

# and (ambas deben ser verdaderas)
a = 5
resultado = a > 0 and a < 10
print("¿0 < 5 < 10?", resultado)

edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print("¿Puede conducir?", puede_conducir)

# falso
x = 15
resultado = x > 10 and x < 20
print("¿10 < 15 < 20?", resultado)

"""output
¿0 < 5 < 10? True
¿Puede conducir? True
¿10 < 15 < 20? True
"""
