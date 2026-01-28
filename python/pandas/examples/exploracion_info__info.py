"""
Objetivo: Obtener información general del DataFrame
Referencia: info
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Mostrar información
print(df.info())

"""output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 8 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   id              10 non-null     int64
 1   nombre          10 non-null     object
 2   apellido        10 non-null     object
 3   edad            10 non-null     int64
 4   email           10 non-null     object
 5   departamento    10 non-null     object
 6   salario         10 non-null     int64
 7   fecha_ingreso   10 non-null     object
dtypes: int64(3), object(5)
memory usage: 720.0 bytes
"""
