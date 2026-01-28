"""
Objetivo: crear un DataFrame desde diccionarios o listas
Referencia: DataFrame
Tipo: clase
Nivel: basico
Dataset: ninguno
"""

import pandas as pd

datos = {
    "producto": ["Laptop", "Mouse", "Teclado"],
    "precio": [1200, 25.99, 85.50],
    "stock": [10, 50, 30]
}

df = pd.DataFrame(datos)

print(df)

"""output
    producto    precio  stock
0     Laptop   1200.00     10
1      Mouse     25.99     50
2   Teclado     85.50     30
"""