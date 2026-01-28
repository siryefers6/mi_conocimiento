"""
Objetivo: Verificar si algún elemento es verdadero
Referencia: any
Tipo: función
Nivel: basico
"""

# any con booleans
print(any([False, False, True]))
print(any([False, False, False]))

# any con números
numeros = [0, 0, 0, 1]
print(any(numeros))  # alguno > 0

numeros2 = [0, 0, 0]
print(any(numeros2))  # todos 0

# any con strings vacíos
palabras = ["", "", "hola"]
print(any(palabras))  # uno no vacío

"""output
True
False
True
False
True
"""
