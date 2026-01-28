"""
Objetivo: Desapilar columnas (wide to long format)
Referencia: melt
Tipo: función
Nivel: intermedio
"""

import pandas as pd

# Crear datos en formato wide
data = {
    'nombre': ['Juan', 'María', 'Carlos'],
    'Matemáticas': [95, 88, 78],
    'Historia': [88, 92, 80],
    'Inglés': [90, 91, 75]
}
df = pd.DataFrame(data)

# Melt: convertir a formato long
resultado = pd.melt(
    df,
    id_vars=['nombre'],
    var_name='asignatura',
    value_name='calificacion'
)

print(resultado)

"""output
    nombre    asignatura  calificacion
0     Juan  Matemáticas             95
1    María  Matemáticas             88
2   Carlos  Matemáticas             78
3     Juan      Historia             88
4    María      Historia             92
5   Carlos      Historia             80
6     Juan        Inglés             90
7    María        Inglés             91
8   Carlos        Inglés             75
"""
