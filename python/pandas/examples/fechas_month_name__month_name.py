"""
Objetivo: Obtener el nombre del mes de una fecha
Referencia: .dt.month_name
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Convertir fecha_ingreso a datetime
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])

# Obtener nombre del mes
df['mes_nombre'] = df['fecha_ingreso'].dt.month_name()

print(df[['nombre', 'fecha_ingreso', 'mes_nombre']])

"""output
      nombre fecha_ingreso mes_nombre
0      Juan     2021-03-15      March
1     María     2019-07-22       July
2    Carlos     2018-01-10     January
3       Ana     2022-05-18         May
4     Pedro     2015-11-01    November
5     Laura     2020-09-30   September
6    Miguel     2023-01-12     January
7     Isabel     2019-04-05       April
8  Francisco     2016-08-20      August
9      Elena     2021-12-08    December
"""
