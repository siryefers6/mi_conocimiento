"""
Objetivo: analizar la estructura del DataFrame y los tipos de datos
Referencia: info
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación
estructura = df.info()

# resultado
print(estructura)

"""output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 10 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   fecha        10 non-null     object
 1   producto_id  10 non-null     int64
 2   producto     10 non-null     object
 3   categoria    10 non-null     object
 4   precio       10 non-null     object
 5   stock        9 non-null      float64
 6   ventas       9 non-null      float64
 7   canal        10 non-null     object
 8   descuento    8 non-null      float64
 9   cliente_id   9 non-null      object
dtypes: float64(3), int64(1), object(6)
memory usage: 932.0+ bytes
None
"""
