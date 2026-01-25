"""
Objetivo: inspeccionar el tipo de una variable
Referencia: type
Tipo: funcion
Nivel: basico
"""

# imports
# no aplica

# carga de datos
numero = 10
texto = "hola"
estado = True

# transformación
tipo_numero = type(numero)
tipo_texto = type(texto)
tipo_estado = type(estado)

# resultado
print(tipo_numero)
print(tipo_texto)
print(tipo_estado)

"""output
<class 'int'>
<class 'str'>
<class 'bool'>
"""
