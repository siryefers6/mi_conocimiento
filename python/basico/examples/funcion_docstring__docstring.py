"""
Objetivo: Documentar funciones con docstrings
Referencia: \"\"\"
Tipo: literal
Nivel: basico
"""

# función con docstring
def suma(a, b):
    """
    Suma dos números y devuelve el resultado.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        La suma de a y b
    """
    return a + b

print(suma(5, 3))
print(suma.__doc__)

# docstring de una línea
def doble(x):
    """Devuelve el doble de un número."""
    return x * 2

print(doble(4))

"""output
8
Suma dos números y devuelve el resultado.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        La suma de a y b
    
8
"""
