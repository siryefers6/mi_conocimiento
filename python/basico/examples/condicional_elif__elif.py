"""
Objetivo: Evaluar múltiples condiciones
Referencia: elif
Tipo: keyword
Nivel: basico
"""

# if-elif-else
calificacion = 7
if calificacion >= 9:
    print("Sobresaliente")
elif calificacion >= 7:
    print("Bien")
elif calificacion >= 5:
    print("Aprobado")
else:
    print("Desaprobado")

# múltiples elif
edad = 25
if edad < 13:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Jubilado")

"""output
Bien
Adulto
"""
