"""
Objetivo: Eliminar todos los pares de un diccionario
Referencia: clear
Tipo: método
Nivel: basico
"""

# limpiar diccionario
datos = {"a": 1, "b": 2, "c": 3}
print("Original:", datos)

datos.clear()
print("Después de clear():", datos)
print("Vacío:", len(datos) == 0)

"""output
Original: {'a': 1, 'b': 2, 'c': 3}
Después de clear(): {}
Vacío: True
"""
