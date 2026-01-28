"""
Objetivo: Guardar DataFrame en archivo JSON
Referencia: to_json
Tipo: método
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'id': [1, 2, 3],
    'nombre': ['Juan', 'María', 'Carlos'],
    'edad': [28, 34, 45]
}
df = pd.DataFrame(data)

# Guardar como JSON en formato registros
df.to_json('datos_guardado.json', orient='records', indent=2)

# Leer de vuelta para verificar
resultado = pd.read_json('datos_guardado.json')
print(resultado)

"""output
   id   nombre  edad
0   1     Juan    28
1   2    María    34
2   3   Carlos    45
"""
