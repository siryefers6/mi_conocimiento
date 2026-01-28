"""
Objetivo: Evaluar si al menos una condición es verdadera
Referencia: or
Tipo: operador
Nivel: basico
"""

# or (al menos una debe ser verdadera)
a = 5
resultado = a < 0 or a > 10
print("¿5 < 0 o 5 > 10?", resultado)

es_fin_de_semana = True
es_feriado = False
no_hay_trabajo = es_fin_de_semana or es_feriado
print("¿No hay trabajo?", no_hay_trabajo)

x = 7
resultado = x < 5 or x > 10
print("¿7 < 5 o 7 > 10?", resultado)

"""output
¿5 < 0 o 5 > 10? False
¿No hay trabajo? True
¿7 < 5 o 7 > 10? False
"""
