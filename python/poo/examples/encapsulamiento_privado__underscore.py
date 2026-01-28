"""
Objetivo: Usar atributos privados con _
Referencia: _atributo
Tipo: convención
Nivel: basico
"""

class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
    
    def obtener_saldo(self):
        return self._saldo

cuenta = CuentaBancaria(1000)
print(f"Saldo: {cuenta.obtener_saldo()}")

cuenta.depositar(500)
print(f"Después depósito: {cuenta.obtener_saldo()}")

# se puede acceder pero no se debe
print(f"Acceso directo (no recomendado): {cuenta._saldo}")

"""output
Saldo: 1000
Después depósito: 1500
Acceso directo (no recomendado): 1500
"""
