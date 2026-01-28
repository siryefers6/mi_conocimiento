"""
Objetivo: Sumar valores de una columna
Referencia: sum
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Sumar salarios
resultado = df['salario'].sum()
print(f"Total de salarios: ${resultado:,.2f}")

# Suma por departamento
resultado_grupo = df.groupby('departamento')['salario'].sum()
print("\nSuma por departamento:")
print(resultado_grupo)

"""output
Total de salarios: $616,000.00

Suma por departamento:
departamento
Dirección          95000
Finanzas          157000
IT                187000
Recursos Humanos   48000
Ventas            147000
Name: salario, dtype: int64
"""
