"""
Objetivo: Crear métodos estáticos con @staticmethod
Referencia: @staticmethod
Tipo: decorador
Nivel: basico
"""

class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b

# no requiere instancia
print(f"Suma: {Matematica.sumar(10, 5)}")
print(f"Multiplicación: {Matematica.multiplicar(4, 3)}")

# también funciona en instancia
math = Matematica()
print(f"Resta indirecta: {math.sumar(8, 2)}")

"""output
Suma: 15
Multiplicación: 12
Resta indirecta: 10
"""
