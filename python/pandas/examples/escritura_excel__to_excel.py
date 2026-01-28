"""
Objetivo: Guardar DataFrame en archivo Excel
Referencia: to_excel
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/productos.csv')

# Guardar en Excel sin índice
df.to_excel('productos_guardado.xlsx', index=False, sheet_name='Productos')

# Leer de vuelta para verificar
resultado = pd.read_excel('productos_guardado.xlsx', sheet_name='Productos')
print(resultado.head())

"""output
   id                nombre categoria  precio  stock      proveedor
0 101             Laptop Pro Electrónica    1200      15      TechCorp
1 102            Monitor 4K Electrónica     500       8  DisplayWorld
2 103      Teclado Mecánico Accesorios     250.5      45     KeyMaster
3 104           Mouse Óptico Accesorios     75.5     120 InputDevices
4 105           Webcam 1080p Electrónica    1200       5      CamWorks
"""
