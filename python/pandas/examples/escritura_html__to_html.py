"""
Objetivo: Guardar DataFrame como tabla HTML
Referencia: to_html
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos pequeños
df = pd.read_csv('../datasets/productos.csv').head(3)

# Guardar como HTML
html = df.to_html()
print(html)

"""output
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>nombre</th>
      <th>categoria</th>
      <th>precio</th>
      <th>stock</th>
      <th>proveedor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>Laptop Pro</td>
      <td>Electrónica</td>
      <td>1200.00</td>
      <td>15</td>
      <td>TechCorp</td>
    </tr>
    <tr>
      <th>1</th>
      <td>102</td>
      <td>Monitor 4K</td>
      <td>Electrónica</td>
      <td>500.00</td>
      <td>8</td>
      <td>DisplayWorld</td>
    </tr>
    <tr>
      <th>2</th>
      <td>103</td>
      <td>Teclado Mecánico</td>
      <td>Accesorios</td>
      <td>250.50</td>
      <td>45</td>
      <td>KeyMaster</td>
    </tr>
  </tbody>
</table>
"""
