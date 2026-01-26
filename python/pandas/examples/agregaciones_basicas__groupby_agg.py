"""
Objetivo: Calcular agregaciones básicas sobre grupos de datos
Referencia: sum, mean, min, max, count
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: agrupar por categoría y calcular suma, promedio, mínimo y máximo de ventas
df_agregaciones = df.groupby('categoria')['ventas'].agg(['sum', 'mean', 'min', 'max']).reset_index()

# Resultado
print(df_agregaciones)

"""output
    categoria   sum  mean   min   max
0  accesorios  60.0  60.0  60.0  60.0
1     oficina   3.0   1.0   0.0   2.0
2  tecnologia  51.0  10.2   4.0  20.0
"""
