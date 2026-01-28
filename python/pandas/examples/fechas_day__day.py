"""
Objetivo: Extraer el día de una columna de fecha
Referencia: .dt.day
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Convertir fecha_ingreso a datetime
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])

# Extraer día
df['dia_ingreso'] = df['fecha_ingreso'].dt.day

print(df[['nombre', 'fecha_ingreso', 'dia_ingreso']])

"""output
      nombre fecha_ingreso  dia_ingreso
0      Juan     2021-03-15           15
1     María     2019-07-22           22
2    Carlos     2018-01-10           10
3       Ana     2022-05-18           18
4     Pedro     2015-11-01            1
5     Laura     2020-09-30           30
6    Miguel     2023-01-12           12
7     Isabel     2019-04-05            5
8  Francisco     2016-08-20           20
9      Elena     2021-12-08            8
"""
