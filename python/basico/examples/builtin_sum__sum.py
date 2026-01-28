"""
Objetivo: Sumar todos los elementos
Referencia: sum
Tipo: función
Nivel: basico
"""

# suma de lista
numeros = [1, 2, 3, 4, 5]
total = sum(numeros)
print(f"Suma: {total}")

# suma con valor inicial
valores = [10, 20, 30]
total2 = sum(valores, 100)
print(f"Suma con inicio: {total2}")

# suma de rango
resultado = sum(range(1, 6))
print(f"Suma 1-5: {resultado}")

"""output
Suma: 15
Suma con inicio: 160
Suma 1-5: 15
"""
