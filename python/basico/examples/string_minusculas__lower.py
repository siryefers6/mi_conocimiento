"""
Objetivo: Convertir una cadena a minúsculas
Referencia: lower
Tipo: método
Nivel: basico
"""

# convertir a minúsculas
texto = "HOLA MUNDO"
resultado = texto.lower()
print(resultado)

# comparación case-insensitive
entrada = "PYTHON"
if entrada.lower() == "python":
    print("Es Python (case-insensitive)")

"""output
hola mundo
Es Python (case-insensitive)
"""
