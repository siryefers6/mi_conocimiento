"""
Objetivo: Aplicar función dentro de cada grupo (sin agregar)
Referencia: groupby().transform
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Normalizando salarios por departamento (restar media del departamento)
df['salario_normalizado'] = df.groupby('departamento')['salario'].transform(
    lambda x: x - x.mean()
)

print(df[['nombre', 'departamento', 'salario', 'salario_normalizado']])

"""output
      nombre departamento  salario  salario_normalizado
0      Juan       Ventas    45000            -4000.0
1     María           IT    65000             2666.667
2    Carlos      Finanzas    75000            -3500.0
3       Ana           IT    62000              -333.333
4     Pedro      Dirección    95000               0.0
5     Laura       Ventas    52000             3000.0
6    Miguel           IT    58000            -4333.333
7     Isabel Recursos Humanos 48000                0.0
8  Francisco      Finanzas    82000             3500.0
9      Elena       Ventas    50000             1000.0
"""
