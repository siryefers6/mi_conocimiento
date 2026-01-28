"""
Objetivo: Organizar tests en carpetas
Referencia: tests/
Tipo: estructura
Nivel: basico
"""

# ESTRUCTURA RECOMENDADA:

# proyecto/
#  src/
#     calculadora.py
#     usuarios.py
#     api.py
#  tests/
#     conftest.py (fixtures compartidas)
#     test_calculadora.py
#     test_usuarios.py
#     integration/
#        test_api.py
#     unit/
#         test_suma.py
#         test_resta.py
#  pytest.ini
#  README.md

# VENTAJAS:
# - Tests separados del código
# - Fácil de navegar
# - Mantiene estructura clara
# - pytest.ini en raíz para config global

# EJECUTAR SOLO UNIT TESTS:
# pytest tests/unit/

# EJECUTAR SOLO INTEGRATION:
# pytest tests/integration/

# EJECUTAR TODO:
# pytest tests/

"""
