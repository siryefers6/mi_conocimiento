"""
Objetivo: Crear generador dentro de clase
Referencia: yield
Tipo: método especial
Nivel: basico
"""

class ContadorDe:
    def __init__(self, maximo):
        self.maximo = maximo
    
    def generar(self):
        for i in range(1, self.maximo + 1):
            yield i

contador = ContadorDe(5)
for numero in contador.generar():
    print(f"Número: {numero}")

"""output
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
"""
