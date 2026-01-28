"""
Objetivo: Verificar si una subcadena existe en una cadena
Referencia: in
Tipo: operador
Nivel: basico
"""

# verificar contenido
texto = "Python es genial"
print("Python" in texto)
print("java" in texto)

# usar en condicional
palabra = "hola"
frase = "hola mundo"
if palabra in frase:
    print("La palabra existe")

# no contenido
print("xyz" not in texto)

"""output
True
False
La palabra existe
True
"""
