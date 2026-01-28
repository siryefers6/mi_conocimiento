"""
Objetivo: Calcular producto acumulado de valores
Referencia: cumprod
Tipo: método
Nivel: avanzado
"""

import pandas as pd

# Crear datos de tasas de crecimiento
data = {
    'año': [2020, 2021, 2022, 2023],
    'tasa_crecimiento': [1.05, 1.08, 1.06, 1.10]  # 5%, 8%, 6%, 10%
}
df = pd.DataFrame(data)

# Calcular producto acumulado (crecimiento compuesto)
df['crecimiento_acumulado'] = df['tasa_crecimiento'].cumprod()

print(df)

"""output
  año  tasa_crecimiento  crecimiento_acumulado
0 2020              1.05                  1.0500
1 2021              1.08                  1.1340
2 2022              1.06                  1.2000
3 2023              1.10                  1.3200
"""
