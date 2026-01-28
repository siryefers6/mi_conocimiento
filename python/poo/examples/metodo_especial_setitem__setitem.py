"""
Objetivo: Implementar __setitem__ para asignación
Referencia: __setitem__
Tipo: método especial
Nivel: basico
"""

class Contenedor:
    def __init__(self):
        self.datos = {}
    
    def __setitem__(self, clave, valor):
        self.datos[clave] = valor
    
    def __getitem__(self, clave):
        return self.datos[clave]

cont = Contenedor()
cont["nombre"] = "Ana"
cont["edad"] = 30

print(f"Nombre: {cont['nombre']}")
print(f"Edad: {cont['edad']}")

cont["edad"] = 31
print(f"Edad actualizada: {cont['edad']}")

"""output
Nombre: Ana
Edad: 30
Edad actualizada: 31
"""
