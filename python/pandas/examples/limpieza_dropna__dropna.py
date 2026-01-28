"""
Objetivo: Eliminar filas con valores nulos
Referencia: dropna
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos con valores faltantes
df = pd.read_csv('../datasets/frutas.csv')

# Mostrar datos originales
print("Datos originales:")
print(df)

# Eliminar filas con cualquier valor nulo
resultado = df.dropna()
print("\nDespués de dropna():")
print(resultado)

"""output
Datos originales:
   id  producto  cantidad  precio   fecha
0   1   Manzana       10.0     0.50  2024-01-01
1   2   Plátano       15.0     0.30  2024-01-01
2   3    Naranja        8.0      NaN  2024-01-02
3   4   Manzana       12.0     0.50  2024-01-02
4   5   Plátano        NaN     0.30  2024-01-03
5   6      Uva       20.0     1.20  2024-01-03
6   7    Naranja        5.0     0.75  2024-01-04
7   8    Fresa        NaN     0.80  2024-01-04
8   9   Manzana       14.0     0.50  2024-01-05
9  10   Plátano       18.0     0.30  2024-01-05

Después de dropna():
   id  producto  cantidad  precio   fecha
0   1   Manzana       10.0     0.50  2024-01-01
1   2   Plátano       15.0     0.30  2024-01-01
3   4   Manzana       12.0     0.50  2024-01-02
5   6      Uva       20.0     1.20  2024-01-03
6   7    Naranja        5.0     0.75  2024-01-04
8   9   Manzana       14.0     0.50  2024-01-05
9  10   Plátano       18.0     0.30  2024-01-05
"""
