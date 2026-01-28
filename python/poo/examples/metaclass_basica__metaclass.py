"""
Objetivo: Introducción a metaclases
Referencia: metaclass
Tipo: patrón avanzado
Nivel: basico
"""

class MiMetaclase(type):
    def __new__(cls, nombre, bases, diccionario):
        print(f"Creando clase: {nombre}")
        return super().__new__(cls, nombre, bases, diccionario)

class MiClase(metaclass=MiMetaclase):
    def __init__(self, valor):
        self.valor = valor

# instantiate
obj = MiClase(42)
print(f"Valor: {obj.valor}")

"""output
Creando clase: MiClase
Valor: 42
"""
