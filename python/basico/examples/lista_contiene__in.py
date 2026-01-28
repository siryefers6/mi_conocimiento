"""
Objetivo: Verificar si un elemento existe en una lista
Referencia: in
Tipo: operador
Nivel: basico
"""

# verificar existencia
numeros = [1, 2, 3, 4, 5]
print(3 in numeros)
print(10 in numeros)

# con strings
frutas = ["manzana", "plátano", "cereza"]
print("manzana" in frutas)
print("uva" in frutas)

# uso en condicional
if "plátano" in frutas:
    print("Tenemos plátano")

# negación
print(99 not in numeros)

"""output
True
False
True
False
Tenemos plátano
True
"""
