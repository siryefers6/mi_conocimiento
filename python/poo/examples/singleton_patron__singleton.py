"""
Objetivo: Implementar patrón Singleton
Referencia: Singleton
Tipo: patrón
Nivel: basico
"""

class ConexionDB:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.conectado = False
        return cls._instancia
    
    def conectar(self):
        self.conectado = True
        return "Conectado a BD"

db1 = ConexionDB()
print(f"ID db1: {id(db1)}")
print(db1.conectar())

db2 = ConexionDB()
print(f"ID db2: {id(db2)}")
print(f"¿Misma instancia? {db1 is db2}")
print(f"Estado conectado: {db2.conectado}")

"""output
ID db1: 140...
ID db2: 140...
¿Misma instancia? True
Estado conectado: True
"""
