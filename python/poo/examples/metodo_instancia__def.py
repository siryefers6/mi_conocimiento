"""
Objetivo: Definir métodos de instancia
Referencia: def
Tipo: keyword
Nivel: basico
"""

class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado
    
    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

calc = Calculadora()
print(f"Suma: {calc.sumar(5, 3)}")
print(f"Resultado almacenado: {calc.resultado}")
print(f"Multiplicación: {calc.multiplicar(4, 7)}")
print(f"Resultado almacenado: {calc.resultado}")

"""output
Suma: 8
Resultado almacenado: 8
Multiplicación: 28
Resultado almacenado: 28
"""
