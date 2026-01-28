"""
Objetivo: Obtener el día de la semana de una fecha
Referencia: .dt.dayofweek
Tipo: método
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'fecha': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']),
    'evento': ['Evento A', 'Evento B', 'Evento C', 'Evento D']
}
df = pd.DataFrame(data)

# Obtener día de semana (0=lunes, 6=domingo)
df['dia_semana'] = df['fecha'].dt.dayofweek
df['nombre_dia'] = df['fecha'].dt.day_name()

print(df)

"""output
      fecha      evento  dia_semana   nombre_dia
0 2024-01-01  Evento A           0      Monday
1 2024-01-02  Evento B           1     Tuesday
2 2024-01-03  Evento C           2   Wednesday
3 2024-01-04  Evento D           3    Thursday
"""
