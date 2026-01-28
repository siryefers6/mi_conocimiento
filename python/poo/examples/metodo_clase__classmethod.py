"""
Objetivo: Crear métodos de clase con @classmethod
Referencia: @classmethod
Tipo: decorador
Nivel: basico
"""

class Temperatura:
    escala = "Celsius"
    
    @classmethod
    def cambiar_escala(cls, nueva_escala):
        cls.escala = nueva_escala
    
    @classmethod
    def obtener_escala(cls):
        return cls.escala

print(f"Escala: {Temperatura.obtener_escala()}")
Temperatura.cambiar_escala("Fahrenheit")
print(f"Escala nueva: {Temperatura.obtener_escala()}")

"""output
Escala: Celsius
Escala nueva: Fahrenheit
"""
