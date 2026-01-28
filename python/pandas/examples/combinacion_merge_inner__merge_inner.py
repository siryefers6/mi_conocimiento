"""
Objetivo: Combinar dos DataFrames por columna común (inner join)
Referencia: merge
Tipo: función
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df_personas = pd.read_csv('../datasets/personas.csv')
df_ventas = pd.read_csv('../datasets/ventas.csv')

# Merge inner: solo coincidencias
resultado = pd.merge(
    df_ventas,
    df_personas[['id', 'nombre', 'departamento']],
    left_on='id_empleado',
    right_on='id',
    how='inner'
)

print(resultado[['nombre', 'departamento', 'cantidad', 'fecha_venta']])

"""output
     nombre departamento  cantidad fecha_venta
0      Juan       Ventas         5  2024-01-05
1      Juan       Ventas         3  2024-01-12
2     María           IT         2  2024-01-15
3     Laura       Ventas         8  2024-01-20
4    Miguel           IT         1  2024-02-03
5      Juan       Ventas         4  2024-02-10
6     Laura       Ventas         6  2024-02-18
7     María           IT         2  2024-02-25
8    Miguel           IT        10  2024-03-02
9      Juan       Ventas         3  2024-03-10
10    Laura       Ventas         7  2024-03-15
11    María           IT         5  2024-03-20
"""
