"""
Objetivo: Trabajar con atributos de instancia
Referencia: self.atributo
Tipo: atributo
Nivel: basico
"""

# atributos de instancia
class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad

cuenta = Banco("Ana", 1000)
print(f"Titular: {cuenta.titular}, Saldo: {cuenta.saldo}")

cuenta.depositar(500)
print(f"Después de depositar: {cuenta.saldo}")

cuenta.retirar(300)
print(f"Después de retirar: {cuenta.saldo}")

"""output
Titular: Ana, Saldo: 1000
Después de depositar: 1500
Después de retirar: 1200
"""
