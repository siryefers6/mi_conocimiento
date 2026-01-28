"""
Objetivo: Extraer el año de una columna de fecha
Referencia: .dt.year
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Convertir fecha_ingreso a datetime
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])

# Extraer año
df['año_ingreso'] = df['fecha_ingreso'].dt.year

print(df[['nombre', 'fecha_ingreso', 'año_ingreso']])

"""output
      nombre fecha_ingreso  año_ingreso
0      Juan     2021-03-15         2021
1     María     2019-07-22         2019
2    Carlos     2018-01-10         2018
3       Ana     2022-05-18         2022
4     Pedro     2015-11-01         2015
5     Laura     2020-09-30         2020
6    Miguel     2023-01-12         2023
7     Isabel     2019-04-05         2019
8  Francisco     2016-08-20         2016
9      Elena     2021-12-08         2021
"""
