"""
Objetivo: Encontrar el índice de la primera ocurrencia de un valor
Referencia: index
Tipo: método
Nivel: basico
"""

# encontrar índice
frutas = ["manzana", "plátano", "cereza"]
indice = frutas.index("plátano")
print(f"'plátano' está en índice {indice}")

# encontrar número
numeros = [10, 20, 30, 20, 40]
print(f"Primer 20 está en índice {numeros.index(20)}")

# error si no existe
# frutas.index("uva")  # ValueError

"""output
'plátano' está en índice 1
Primer 20 está en índice 1
"""
