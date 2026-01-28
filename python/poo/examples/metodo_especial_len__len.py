"""
Objetivo: Implementar __len__ para obtener longitud
Referencia: __len__
Tipo: método especial
Nivel: basico
"""

class Lista:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __len__(self):
        return len(self.elementos)

lista = Lista([1, 2, 3, 4, 5])
print(f"Longitud: {len(lista)}")

lista2 = Lista(["a", "b"])
print(f"Longitud: {len(lista2)}")

"""output
Longitud: 5
Longitud: 2
"""
