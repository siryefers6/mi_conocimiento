"""
Objetivo: Crear una tupla con un solo elemento
Referencia: ()
Tipo: literal
Nivel: basico
"""

# un elemento SIN coma es solo el valor
solo_numero = (5)
print("Sin coma:", solo_numero, "Tipo:", type(solo_numero))

# un elemento CON coma es tupla
tupla_uno = (5,)
print("Con coma:", tupla_uno, "Tipo:", type(tupla_uno))

# vacía
vacia = ()
print("Vacía:", vacia, "Tipo:", type(vacia))

"""output
Sin coma: 5 Tipo: <class 'int'>
Con coma: (5,) Tipo: <class 'tuple'>
Vacía: () Tipo: <class 'tuple'>
"""
