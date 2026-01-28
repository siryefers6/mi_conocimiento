"""
Objetivo: Guardar DataFrame en base de datos SQL
Referencia: to_sql
Tipo: método
Nivel: intermedio
"""

import pandas as pd
import sqlite3

# Cargar datos
df = pd.read_csv('../datasets/productos.csv')

# Crear conexión
conn = sqlite3.connect(':memory:')

# Guardar en SQL
df.to_sql('productos', conn, index=False, if_exists='replace')

# Leer de vuelta
resultado = pd.read_sql('SELECT * FROM productos LIMIT 3', conn)
print("Datos guardados en SQL:")
print(resultado)

conn.close()

"""output
    id             nombre categoria   precio  stock    proveedor
0  101        Laptop Pro Electrónica  1200.00     15     TechCorp
1  102         Monitor 4K Electrónica   500.00      8  DisplayWorld
2  103   Teclado Mecánico Accesorios   250.50     45    KeyMaster
"""
