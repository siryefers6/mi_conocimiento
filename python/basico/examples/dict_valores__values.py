"""
Objetivo: Obtener todos los valores de un diccionario
Referencia: values
Tipo: método
Nivel: basico
"""

# obtener valores
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
valores = persona.values()
print("Valores:", valores)
print("Como lista:", list(valores))

# iterar sobre valores
for valor in persona.values():
    print(valor)

"""output
Valores: dict_values(['Ana', 30, 'Madrid'])
Como lista: ['Ana', 30, 'Madrid']
Ana
30
Madrid
"""
