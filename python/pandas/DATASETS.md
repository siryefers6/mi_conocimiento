# Datasets para Pandas - Documentación

Estos datasets están diseñados para cubrir casos de uso reales en análisis de datos.

---

## personas.csv (10 registros)

**Propósito:** Demostrar operaciones básicas con datos de empleados.

**Columnas:**
- `id` (int): Identificador único
- `nombre` (str): Nombre del empleado
- `apellido` (str): Apellido
- `edad` (int): Edad (rango: 27-55)
- `email` (str): Email corporativo
- `departamento` (str): Área de trabajo (Ventas, IT, Finanzas, etc.)
- `salario` (int): Salario anual
- `fecha_ingreso` (str): Fecha de ingreso (YYYY-MM-DD)

**Casos de uso:**
- Filtrado y selección
- Groupby por departamento
- Cálculos de estadísticas
- Transformación de fechas
- Alineación de índices

---

## ventas.csv (12 registros)

**Propósito:** Demostrar transacciones con múltiples dimensiones para merges.

**Columnas:**
- `id_venta` (int): ID de transacción
- `id_empleado` (int): ID del vendedor (referencia a personas.csv)
- `id_producto` (int): ID del producto (referencia a productos.csv)
- `cantidad` (int): Unidades vendidas
- `fecha_venta` (str): Fecha de venta (YYYY-MM-DD)
- `precio_unitario` (float): Precio por unidad
- `region` (str): Región (Norte, Este, Oeste)

**Casos de uso:**
- Merge/join con personas y productos
- Agregaciones por fecha
- Cálculos de ingresos
- Groupby por región/empleado
- Resample temporal

---

## productos.csv (8 registros)

**Propósito:** Demostrar catálogo de datos con diferentes categorías.

**Columnas:**
- `id` (int): ID del producto
- `nombre` (str): Nombre del producto
- `categoria` (str): Tipo (Electrónica, Accesorios)
- `precio` (float): Precio unitario
- `stock` (int): Cantidad en inventario
- `proveedor` (str): Nombre del proveedor

**Casos de uso:**
- Merge con ventas
- Filtrado por categoría
- Cálculos de inventario
- Groupby por proveedor

---

## calificaciones.csv (8 registros)

**Propósito:** Demostrar datos multicolumnares para correlaciones.

**Columnas:**
- `id_estudiante` (int): ID único
- `nombre` (str): Nombre del estudiante
- `matematica` (int): Nota (0-100)
- `fisica` (int): Nota (0-100)
- `historia` (int): Nota (0-100)
- `inglés` (int): Nota (0-100)
- `año` (int): Año académico

**Casos de uso:**
- Análisis de correlación entre materias
- Cálculo de promedios
- Identificación de estudiantes destacados
- Análisis estadístico descriptivo
- Covarianza entre variables

---

## clima.csv (10 registros)

**Propósito:** Demostrar series de tiempo con múltiples ciudades.

**Columnas:**
- `fecha` (str): Fecha (YYYY-MM-DD)
- `ciudad` (str): Nombre de ciudad (Madrid, Barcelona, Valencia)
- `temperatura_max` (float): Máxima del día
- `temperatura_min` (float): Mínima del día
- `humedad` (int): Porcentaje (0-100)
- `precipitacion` (float): mm de lluvia

**Casos de uso:**
- Resample y agregación temporal
- Groupby por ciudad
- Cálculo de promedios
- Operaciones con fechas
- Análisis de tendencias

---

## frutas.csv (10 registros)

**Propósito:** Demostrar limpieza de datos con valores faltantes.

**Columnas:**
- `id` (int): Identificador
- `producto` (str): Nombre de la fruta
- `cantidad` (float): Unidades (¡CONTIENE NaN!)
- `precio` (float): Precio unitario (¡CONTIENE NaN!)
- `fecha` (str): Fecha de registro

**Valores faltantes:**
- Row 2: precio = NaN
- Row 4: cantidad = NaN
- Row 7: cantidad = NaN

**Casos de uso:**
- `dropna()` para eliminar valores faltantes
- `fillna()` para rellenar
- `interpolate()` para interpolar
- `isnull()` para detectar
- Prácticas de limpieza de datos

---

## Relaciones entre datasets

```
personas.csv ──┐
               ├─→ ventas.csv ─→ productos.csv
productos.csv ─┘
```

**Claves de unión:**
- `personas.csv.id` = `ventas.csv.id_empleado`
- `productos.csv.id` = `ventas.csv.id_producto`

---

## Cómo usar los datasets en ejemplos

```python
import pandas as pd

# Lectura simple
df = pd.read_csv('datasets/personas.csv')

# Merge
df_merged = pd.merge(ventas, personas, 
                     left_on='id_empleado', 
                     right_on='id')

# Análisis
resultado = df.groupby('departamento')['salario'].mean()
```

---

## Estadísticas rápidas

| Dataset | Filas | Columnas | Tipos | Nulos | Uso |
|---------|-------|----------|-------|-------|-----|
| personas.csv | 10 | 8 | int, str | No | Basico |
| ventas.csv | 12 | 7 | int, str, float | No | Merge, Temporal |
| productos.csv | 8 | 6 | int, str, float | No | Categorización |
| calificaciones.csv | 8 | 7 | int, str | No | Correlación |
| clima.csv | 10 | 6 | str, float, int | No | Series Tiempo |
| frutas.csv | 10 | 5 | int, str, float | Sí | Limpieza |

---

## Extensiones futuras

Considerar agregar:
- Dataset de ventas con 1000+ registros para operaciones a escala
- Dataset de series temporales largas (años de datos)
- Dataset con datos de texto para NLP
- Dataset con múltiples tipos de datos faltantes
- Dataset con outliers para detección anómala
