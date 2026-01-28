"""
Objetivo: Leer datos de archivo Excel
Referencia: read_excel
Tipo: función
Nivel: basico
"""

import pandas as pd

# Primero crear un archivo Excel de ejemplo
data = {
    'id': [1, 2, 3, 4, 5],
    'producto': ['Laptop', 'Monitor', 'Teclado', 'Mouse', 'Webcam'],
    'precio': [1200, 500, 150, 75, 1200]
}
df_temp = pd.DataFrame(data)
df_temp.to_excel('productos_ejemplo.xlsx', index=False)

# Leer archivo Excel
df = pd.read_excel('productos_ejemplo.xlsx')

print("Datos leídos de Excel:")
print(df)

"""output
   id  producto  precio
0   1    Laptop    1200
1   2   Monitor     500
2   3   Teclado     150
3   4     Mouse      75
4   5    Webcam    1200
"""
