"""
Objetivo: Usar atributos compartidos por toda la clase
Referencia: Clase.atributo
Tipo: atributo
Nivel: basico
"""

# atributo de clase
class Contador:
    total = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Contador.total += 1
    
    @classmethod
    def cuantos(cls):
        return cls.total

c1 = Contador("primero")
print(f"Total: {Contador.total}")

c2 = Contador("segundo")
print(f"Total: {Contador.total}")

c3 = Contador("tercero")
print(f"Total con método: {Contador.cuantos()}")

"""output
Total: 1
Total: 2
Total con método: 3
"""
