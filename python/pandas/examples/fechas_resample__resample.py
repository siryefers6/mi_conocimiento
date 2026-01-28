"""
Objetivo: Cambiar frecuencia temporal de datos (resamplear)
Referencia: resample
Tipo: método
Nivel: avanzado
"""

import pandas as pd

# Crear datos de series de tiempo
dates = pd.date_range('2024-01-01', periods=30, freq='D')
data = {
    'fecha': dates,
    'ventas': [100, 150, 120, 180, 200, 160, 140, 190, 210, 180,
               170, 220, 240, 200, 190, 210, 250, 230, 210, 200,
               180, 220, 240, 260, 280, 250, 230, 220, 210, 190]
}
df = pd.DataFrame(data)
df = df.set_index('fecha')

# Resamplear a frecuencia semanal (suma)
resultado_semanal = df.resample('W').sum()
print("Ventas semanales (suma):")
print(resultado_semanal)

"""output
            ventas
fecha
2024-01-07    1050
2024-01-14    1310
2024-01-21    1630
2024-01-28    1360
"""
