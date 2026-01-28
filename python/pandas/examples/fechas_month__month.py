"""
Objetivo: Extraer el mes de una columna de fecha
Referencia: .dt.month
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Convertir fecha_ingreso a datetime
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])

# Extraer mes
df['mes_ingreso'] = df['fecha_ingreso'].dt.month

print(df[['nombre', 'fecha_ingreso', 'mes_ingreso']])

"""output
      nombre fecha_ingreso  mes_ingreso
0      Juan     2021-03-15            3
1     María     2019-07-22            7
2    Carlos     2018-01-10            1
3       Ana     2022-05-18            5
4     Pedro     2015-11-01           11
5     Laura     2020-09-30            9
6    Miguel     2023-01-12            1
7     Isabel     2019-04-05            4
8  Francisco     2016-08-20            8
9      Elena     2021-12-08           12
"""
