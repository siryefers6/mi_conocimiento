"""
Objetivo: Invertir el valor lógico (negación)
Referencia: not
Tipo: operador
Nivel: basico
"""

# not (invertir lógica)
a = True
print("¿not True?", not a)

b = False
print("¿not False?", not b)

resultado = 5 > 10
print("¿not (5 > 10)?", not resultado)

# negar condición
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir?", puedo_salir)

"""output
¿not True? False
¿not False? True
¿not (5 > 10)? True
¿Puedo salir? True
"""
