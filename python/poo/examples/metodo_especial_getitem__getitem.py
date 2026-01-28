"""
Objetivo: Implementar __getitem__ para indexación
Referencia: __getitem__
Tipo: método especial
Nivel: basico
"""

class Secuencia:
    def __init__(self, datos):
        self.datos = datos
    
    def __getitem__(self, indice):
        return self.datos[indice]
    
    def __len__(self):
        return len(self.datos)

seq = Secuencia([10, 20, 30, 40])
print(f"Elemento 0: {seq[0]}")
print(f"Elemento 2: {seq[2]}")
print(f"Último: {seq[-1]}")
print(f"Slice [1:3]: {seq[1:3]}")

"""output
Elemento 0: 10
Elemento 2: 30
Último: 40
Slice [1:3]: [20, 30]
"""
