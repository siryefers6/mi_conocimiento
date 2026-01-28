"""
Objetivo: Usar atributos altamente privados con __
Referencia: __atributo
Tipo: convención
Nivel: basico
"""

class Caja:
    def __init__(self, contenido):
        self.__contenido = contenido
    
    def abrir(self):
        return self.__contenido
    
    def reemplazar(self, nuevo):
        self.__contenido = nuevo

caja = Caja("sorpresa")
print(f"Contenido: {caja.abrir()}")

# intentar acceso directo falla
try:
    print(caja.__contenido)
except AttributeError:
    print("No se puede acceder a __contenido directamente")

# pero existe mediante name mangling
print(f"Mediante name mangling: {caja._Caja__contenido}")

"""output
Contenido: sorpresa
No se puede acceder a __contenido directamente
Mediante name mangling: sorpresa
"""
