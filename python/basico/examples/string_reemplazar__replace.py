"""
Objetivo: Reemplazar texto dentro de una cadena
Referencia: replace
Tipo: método
Nivel: basico
"""

# reemplazar simple
texto = "Hola mundo"
nuevo = texto.replace("mundo", "Python")
print(nuevo)

# reemplazar múltiple
contenido = "cat cat cat"
resultado = contenido.replace("cat", "dog")
print(resultado)

# reemplazar limitado
frase = "uno uno uno"
resultado = frase.replace("uno", "dos", 2)
print(resultado)

"""output
Hola Python
dog dog dog
dos dos uno
"""
