"""
Objetivo: cargar un CSV definiendo tipos de datos explícitos
Referencia: read_csv
Tipo: funcion
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

# definición de tipos (precio se deja como string por dato mal formateado)
dtypes = {
    "producto_id": "int64",
    "producto": "string",
    "categoria": "string",
    "precio": "string",
    "stock": "float64",
    "ventas": "float64",
    "canal": "string",
    "descuento": "float64",
    "cliente_id": "string",
}

# carga de datos
df = pd.read_csv(
    "datasets/ventas.csv",
    dtype=dtypes
)

# resultado
print(df.dtypes)

"""output
fecha                  object
producto_id             int64
producto       string[python]
categoria      string[python]
precio         string[python]
stock                 float64
ventas                float64
canal          string[python]
descuento             float64
cliente_id     string[python]
dtype: object
"""
