"""
Objetivo: Aplicar una función a los valores de una columna
Referencia: apply
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: aplicar descuento al precio
# Convierte precio a float y aplica el descuento si existe, si no, deja precio original
df['precio_final'] = df.apply(
    lambda row: float(str(row['precio']).replace(' USD','').replace('$','')) * (1 - row['descuento'] if pd.notna(row['descuento']) else 1),
    axis=1
)

# Resultado
print(df[['producto', 'precio', 'descuento', 'precio_final']])

"""output
     producto   precio  descuento  precio_final
0      Laptop     1200       0.10       1080.00
1       Mouse       25        NaN         25.00
2     Teclado       45       0.05         42.75
3       Silla      300       0.15        255.00
4  Escritorio      450       0.20        360.00
5     Monitor  500 USD       0.10        450.00
6   Impresora      250       0.00        250.00
7  Cable HDMI       15        NaN         15.00
8      Webcam       85       0.05         80.75
9      Router      120       0.10        108.00
"""
