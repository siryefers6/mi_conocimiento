"""
Objetivo: Aplicar múltiples agregaciones a datos agrupados
Referencia: agg
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Agregar con múltiples funciones
resultado = df.groupby('departamento').agg({
    'salario': ['sum', 'mean', 'count'],
    'edad': ['min', 'max']
})

print(resultado)

"""output
              salario              age
                 sum        mean count min max
departamento                                    
Dirección       95000  95000.000000    1  51  51
Finanzas       157000  78500.000000    2  45  55
IT             187000  62333.333333    3  27  34
Recursos Humanos 48000  48000.000000    1  38  38
Ventas          147000  49000.000000    3  28  32
"""
