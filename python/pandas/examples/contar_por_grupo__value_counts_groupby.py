"""
Objetivo: Contar la frecuencia de valores agrupados por otra columna
Referencia: value_counts + groupby
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Rellenar valores nulos en 'canal' para evitar errores
df['canal'] = df['canal'].fillna('Desconocido')

# Contar frecuencia de productos por canal
conteo_por_canal = df.groupby('canal')['producto'].value_counts().unstack(fill_value=0)

# Resultado
print(conteo_por_canal)

"""output
producto  Cable HDMI  Escritorio  Impresora  Laptop  Monitor  Mouse  Router  Silla  Teclado  Webcam
canal
online             1           1          0       1        1      0       0      0        1       1
tienda             0           0          1       0        0      1       1      1        0       0
"""
