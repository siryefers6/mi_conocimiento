"""
Objetivo: Crear o modificar pares clave-valor
Referencia: []
Tipo: operador
Nivel: basico
"""

# crear nuevo par
persona = {}
persona["nombre"] = "Juan"
persona["edad"] = 25
print(persona)

# modificar valor existente
persona["edad"] = 26
print(persona)

# agregar más pares
persona["ciudad"] = "Barcelona"
persona["activo"] = True
print(persona)

"""output
{'nombre': 'Juan', 'edad': 25}
{'nombre': 'Juan', 'edad': 26}
{'nombre': 'Juan', 'edad': 26, 'ciudad': 'Barcelona', 'activo': True}
"""
