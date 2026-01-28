"""
Objetivo: Usar condicional en una línea (ternario)
Referencia: if-else
Tipo: expresión
Nivel: basico
"""

# operador ternario
edad = 20
estatus = "mayor" if edad >= 18 else "menor"
print(estatus)

# con variables
numero = 7
resultado = "par" if numero % 2 == 0 else "impar"
print(resultado)

# ternario anidado
calificacion = 8
mensaje = "Excelente" if calificacion >= 9 else "Bueno" if calificacion >= 7 else "Regular"
print(mensaje)

"""output
mayor
impar
Bueno
"""
