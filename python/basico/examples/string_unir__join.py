"""
Objetivo: Unir elementos de una lista en una cadena
Referencia: join
Tipo: método
Nivel: basico
"""

# unir con espacio
palabras = ["Hola", "mundo", "Python"]
resultado = " ".join(palabras)
print(resultado)

# unir con guión
nombres = ["Juan", "Ana", "Carlos"]
resultado = "-".join(nombres)
print(resultado)

# unir números
numeros = ["1", "2", "3"]
resultado = ",".join(numeros)
print(resultado)

"""output
Hola mundo Python
Juan-Ana-Carlos
1,2,3
"""
