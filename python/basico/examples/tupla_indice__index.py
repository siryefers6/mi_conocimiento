"""
Objetivo: Encontrar el índice de un elemento en una tupla
Referencia: index
Tipo: método
Nivel: basico
"""

# encontrar índice
frutas = ("manzana", "plátano", "cereza")
indice = frutas.index("plátano")
print(f"'plátano' está en índice {indice}")

# con números
numeros = (10, 20, 30)
print(f"20 está en índice {numeros.index(20)}")

# error si no existe
# frutas.index("uva")  # ValueError

"""output
'plátano' está en índice 1
20 está en índice 1
"""
