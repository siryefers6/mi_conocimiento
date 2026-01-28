"""
Objetivo: Obtener el número de pares en un diccionario
Referencia: len
Tipo: función
Nivel: basico
"""

# cantidad de pares
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
cantidad = len(persona)
print(f"Diccionario tiene {cantidad} pares")

# diccionario vacío
vacio = {}
print(f"Diccionario vacío: {len(vacio)} pares")

# diccionario grande
datos = {str(i): i*2 for i in range(100)}
print(f"Diccionario grande: {len(datos)} pares")

"""output
Diccionario tiene 3 pares
Diccionario vacío: 0 pares
Diccionario grande: 100 pares
"""
