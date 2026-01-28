"""
Objetivo: Convención de nombres para tests
Referencia: test_*.py
Tipo: convención
Nivel: basico
"""

# CONVENCIÓN DE NOMBRES PARA PYTEST:

#  Nombres correctos (pytest los encuentra):
# - test_suma.py
# - test_usuarios.py
# - tests/test_api.py

#  Nombres incorrectos (pytest NO los encuentra):
# - suma_test.py
# - usuarios.py
# - test-suma.py

# Dentro del archivo:

#  Funciones de test (comienzan con test_):
def test_suma_basica():
    pass

def test_resta_negativos():
    pass

#  No serán ejecutadas:
def suma_basica():  # Sin test_ prefix
    pass

#  Clases de test (comienzan con Test):
class TestCalculadora:
    def test_sumar(self):
        pass
    
    def test_multiplicar(self):
        pass

#  No serán ejecutadas:
class Calculadora:  # Sin Test prefix
    def test_sumar(self):
        pass

"""
