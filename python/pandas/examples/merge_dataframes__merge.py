"""
Objetivo: unir dos DataFrames por una columna común
Referencia: merge
Tipo: funcion
Nivel: intermedio
Dataset: ventas.csv, clientes.csv
"""

import pandas as pd

ventas = pd.read_csv("datasets/ventas.csv")
clientes = pd.read_csv("datasets/clientes.csv")

# Unir ventas con información del cliente
resultado = pd.merge(ventas, clientes, on="cliente_id", how="left")

print(resultado[["producto", "cliente_id", "nombre", "ciudad"]].head())

"""output
            producto cliente_id      nombre       ciudad
0       Laptop ASIS      001      Juan Pérez    Madrid
1     Mouse Logitech      002   María García  Barcelona
2    Teclado Mecánico      003    Carlos López     Valencia
3       Monitor LG 24      004  Ana Rodríguez     Sevilla
4    Escritorio Gamer      005  Pedro Martínez      Bilbao
"""