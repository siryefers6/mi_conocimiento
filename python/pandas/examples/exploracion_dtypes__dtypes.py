"""
Objetivo: Obtener los tipos de datos de cada columna
Referencia: dtypes
Tipo: atributo
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Obtener tipos de datos
print(df.dtypes)

"""output
id               int64
nombre          object
apellido        object
edad            int64
email           object
departamento    object
salario         int64
fecha_ingreso   object
dtype: object
"""
