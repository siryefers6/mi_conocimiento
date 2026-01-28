"""
Objetivo: Ejecutar código después de try-except
Referencia: finally
Tipo: keyword
Nivel: basico
"""

# finally siempre se ejecuta
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Finally ejecutado")

print("---")

# finally sin error también
try:
    x = 5 + 3
    print(f"Resultado: {x}")
except:
    print("Error")
finally:
    print("Finally ejecutado")

"""output
No se puede dividir por cero
Finally ejecutado
---
Resultado: 8
Finally ejecutado
"""
