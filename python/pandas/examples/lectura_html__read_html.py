"""
Objetivo: Extraer tablas de HTML
Referencia: read_html
Tipo: función
Nivel: intermedio
"""

import pandas as pd

# Crear HTML de ejemplo con una tabla
html = """
<html>
  <body>
    <table>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>edad</th>
      </tr>
      <tr>
        <td>1</td>
        <td>Juan</td>
        <td>28</td>
      </tr>
      <tr>
        <td>2</td>
        <td>María</td>
        <td>34</td>
      </tr>
    </table>
  </body>
</html>
"""

# Guardar HTML temporalmente
with open('tabla_temp.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Leer tablas HTML
tablas = pd.read_html('tabla_temp.html')
df = tablas[0]

print("Tabla extraída de HTML:")
print(df)

"""output
   id nombre  edad
0   1   Juan    28
1   2  María    34
"""
