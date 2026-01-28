"""
Objetivo: Cargar datos desde un archivo JSON
Referencia: read_json
Tipo: función
Nivel: basico
"""

import pandas as pd
import json

# Crear datos de ejemplo y guardarlos como JSON
data = {
    'id': [1, 2, 3],
    'nombre': ['Juan', 'María', 'Carlos'],
    'edad': [28, 34, 45]
}
df_original = pd.DataFrame(data)
df_original.to_json('ejemplos_temp.json', orient='records')

# Leer archivo JSON
df = pd.read_json('ejemplos_temp.json')

# Mostrar resultado
print(df)

"""output
   id   nombre  edad
0   1     Juan    28
1   2    María    34
2   3   Carlos    45
"""
