"""
Objetivo: Convertir columna a tipo datetime
Referencia: to_datetime
Tipo: función
Nivel: basico
"""

import pandas as pd

# Crear datos con fechas en formato string
data = {
    'fecha_texto': ['2024-01-15', '2024-02-20', '2024-03-10'],
    'evento': ['Venta', 'Compra', 'Venta']
}
df = pd.DataFrame(data)

# Convertir a datetime
df['fecha'] = pd.to_datetime(df['fecha_texto'])

print("Tipo original:", df['fecha_texto'].dtype)
print("Tipo nuevo:", df['fecha'].dtype)
print("\nDataFrame:")
print(df)

"""output
Tipo original: object
Tipo nuevo: datetime64[ns]

DataFrame:
  fecha_texto evento      fecha
0  2024-01-15   Venta 2024-01-15
1  2024-02-20   Compra 2024-02-20
2  2024-03-10   Venta 2024-03-10
"""
