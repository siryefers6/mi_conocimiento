"""
Objetivo: Encontrar la posición de una subcadena
Referencia: find
Tipo: método
Nivel: basico
"""

# find devuelve el índice
texto = "Hola mundo"
posicion = texto.find("mundo")
print(f"'mundo' está en posición {posicion}")

# no encontrado devuelve -1
resultado = texto.find("xyz")
print(f"'xyz' en posición {resultado}")

# encontrar primer carácter
pos = "Python".find("o")
print(f"Primera 'o' en posición {pos}")

"""output
'mundo' está en posición 5
'xyz' en posición -1
Primera 'o' en posición 4
"""
