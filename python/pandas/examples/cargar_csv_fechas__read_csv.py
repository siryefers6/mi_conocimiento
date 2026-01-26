"""
Objetivo: cargar un CSV parseando columnas de fecha
Referencia: read_csv
Tipo: funcion
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos con parseo de fechas
df = pd.read_csv(
    "datasets/ventas.csv",
    parse_dates=["fecha"]
)

# resultado
print(df.dtypes)
print(df["fecha"].head())

"""output
fecha          datetime64[ns]
producto_id             int64
producto               object
categoria              object
precio                 object
stock                 float64
ventas                float64
canal                  object
descuento             float64
cliente_id             object
dtype: object
0   2024-01-01
1   2024-01-02
2   2024-01-03
3   2024-01-04
4   2024-01-05
Name: fecha, dtype: datetime64[ns]
"""
