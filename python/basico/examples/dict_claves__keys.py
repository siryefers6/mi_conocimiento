"""
Objetivo: Obtener todas las claves de un diccionario
Referencia: keys
Tipo: método
Nivel: basico
"""

# obtener claves
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
claves = persona.keys()
print("Claves:", claves)
print("Como lista:", list(claves))

# iterar sobre claves
for clave in persona.keys():
    print(clave)

"""output
Claves: dict_keys(['nombre', 'edad', 'ciudad'])
Como lista: ['nombre', 'edad', 'ciudad']
nombre
edad
ciudad
"""
