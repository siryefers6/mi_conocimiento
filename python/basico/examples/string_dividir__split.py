"""
Objetivo: Dividir una cadena en una lista de palabras
Referencia: split
Tipo: método
Nivel: basico
"""

# dividir por espacio
texto = "Hola mundo Python"
palabras = texto.split()
print(palabras)

# dividir por delimitador
csv = "Juan,Ana,Carlos"
nombres = csv.split(",")
print(nombres)

# dividir por límite
frase = "uno-dos-tres-cuatro"
partes = frase.split("-", 2)
print(partes)

"""output
['Hola', 'mundo', 'Python']
['Juan', 'Ana', 'Carlos']
['uno', 'dos', 'tres-cuatro']
"""
