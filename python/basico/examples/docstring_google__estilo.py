"""
Objetivo: documentar una función siguiendo la convención Google
Referencia: docstring (Google Style)
Tipo: convencion
Nivel: basico
"""

# imports
# no aplica

# carga de datos
# no aplica

# transformación
def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (int | float): dividendo
        b (int | float): divisor

    Returns:
        float: resultado de la división

    Raises:
        ValueError: si el divisor es cero
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b

# resultado
print(dividir(10, 2))

"""output
5.0
"""
