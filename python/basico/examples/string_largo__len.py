"""
Objetivo: Obtener el número de caracteres en una cadena
Referencia: len
Tipo: función
Nivel: basico
"""

# largo de string
texto = "Hola"
longitud = len(texto)
print(f"'{texto}' tiene {longitud} caracteres")

# otro ejemplo
palabra = "Python"
print(f"'{palabra}' tiene {len(palabra)} caracteres")

# string vacío
vacio = ""
print(f"String vacío tiene {len(vacio)} caracteres")

"""output
'Hola' tiene 4 caracteres
'Python' tiene 6 caracteres
String vacío tiene 0 caracteres
"""
