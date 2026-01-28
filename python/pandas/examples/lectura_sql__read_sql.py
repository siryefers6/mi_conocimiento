"""
Objetivo: Leer datos de base de datos SQL
Referencia: read_sql
Tipo: función
Nivel: intermedio
"""

import pandas as pd
import sqlite3

# Crear conexión a SQLite (base de datos en memoria)
conn = sqlite3.connect(':memory:')

# Crear tabla de ejemplo
data = {
    'id': [1, 2, 3, 4, 5],
    'nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Pedro'],
    'edad': [28, 34, 45, 29, 51]
}
df_temp = pd.DataFrame(data)
df_temp.to_sql('personas', conn, index=False)

# Leer con SQL query
df = pd.read_sql('SELECT * FROM personas WHERE edad > 30', conn)

print("Datos leídos de SQL:")
print(df)

conn.close()

"""output
  id   nombre  edad
0  2    María    34
1  3   Carlos    45
2  5    Pedro    51
"""
