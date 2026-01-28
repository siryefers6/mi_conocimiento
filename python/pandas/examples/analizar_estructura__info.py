"""
Objetivo: obtener información general sobre el DataFrame
Referencia: info
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

df.info()

"""output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 8 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   fecha         20 non-null     object
 1   producto_id   20 non-null     int64
 2   producto      20 non-null     object
 3   categoria     20 non-null     object
 4   precio        20 non-null     float64
 5   stock         20 non-null     int64
 6   descuento     20 non-null     float64
 7   cliente_id    20 non-null     object
"""