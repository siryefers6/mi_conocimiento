"""
Objetivo: Verificar si todos los elementos son verdaderos
Referencia: all
Tipo: función
Nivel: basico
"""

# all con booleans
print(all([True, True, True]))
print(all([True, False, True]))

# all con números
numeros = [1, 2, 3, 4]
print(all(numeros))  # todos > 0

numeros2 = [1, 0, 3]
print(all(numeros2))  # contiene 0 (falso)

# all con strings
palabras = ["hola", "mundo"]
print(all(palabras))  # todos no vacíos

"""output
True
False
True
False
True
"""
