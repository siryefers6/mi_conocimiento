"""
Objetivo: Mapear o reemplazar valores de una columna usando un diccionario
Referencia: map
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: abreviar nombres de categoría
map_categoria = {
    'tecnologia': 'tec',
    'oficina': 'ofi',
    'accesorios': 'acc'
}
df['categoria_abrev'] = df['categoria'].map(map_categoria)

# Resultado
print(df[['producto', 'categoria', 'categoria_abrev']])

"""output
     producto   categoria categoria_abrev
0      Laptop  tecnologia             tec
1       Mouse  tecnologia             tec
2     Teclado  tecnologia             tec
3       Silla     oficina             ofi
4  Escritorio     oficina             ofi
5     Monitor  tecnologia             tec
6   Impresora     oficina             ofi
7  Cable HDMI  accesorios             acc
8      Webcam  accesorios             acc
9      Router  tecnologia             tec
"""
