"""
Objetivo: Implementar __enter__ y __exit__ para context managers
Referencia: __enter__, __exit__
Tipo: método especial
Nivel: basico
"""

class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = None
    
    def __enter__(self):
        print(f"Abriendo {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cerrando {self.nombre}")
        return False

with Archivo("datos.txt") as f:
    print(f"Usando archivo: {f.nombre}")

print("Salió del bloque with")

"""output
Abriendo datos.txt
Usando archivo: datos.txt
Cerrando datos.txt
Salió del bloque with
"""
