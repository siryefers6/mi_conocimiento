"""
Objetivo: Convertir una cadena a mayúsculas
Referencia: upper
Tipo: método
Nivel: basico
"""

# convertir a mayúsculas
texto = "Hola mundo"
resultado = texto.upper()
print(resultado)

# original no cambia
print(texto)

# usar en condicional
entrada = "si"
if entrada.upper() == "SI":
    print("Respuesta afirmativa")

"""output
HOLA MUNDO
Hola mundo
Respuesta afirmativa
"""
