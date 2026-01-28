# Pandas - Guía Completa

Referencia rápida de métodos, operaciones y conceptos fundamentales de Pandas con ejemplos ejecutables.

---

## Instalación y Configuración

### Instalación rápida

```bash
pip install pandas
pip install openpyxl  # para leer/escribir Excel
pip install xlrd      # para leer formatos antiguos
```

### Import estándar

```python
import pandas as pd
import numpy as np
```

---

## Entrada/Salida de Datos (I/O)

### Lectura de datos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Leer CSV | `read_csv` | función | Cargar archivos CSV | [ver](examples/lectura_csv__read_csv.py) |
| Leer Excel | `read_excel` | función | Cargar archivos XLSX | [ver](examples/lectura_excel__read_excel.py) |
| Leer JSON | `read_json` | función | Cargar archivos JSON | [ver](examples/lectura_json__read_json.py) |
| Leer SQL | `read_sql` | función | Cargar desde base de datos | [ver](examples/lectura_sql__read_sql.py) |
| Leer HTML | `read_html` | función | Extraer tablas de HTML | [ver](examples/lectura_html__read_html.py) |

### Escritura de datos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Guardar CSV | `to_csv` | método | Exportar a CSV | [ver](examples/escritura_csv__to_csv.py) |
| Guardar Excel | `to_excel` | método | Exportar a XLSX | [ver](examples/escritura_excel__to_excel.py) |
| Guardar JSON | `to_json` | método | Exportar a JSON | [ver](examples/escritura_json__to_json.py) |
| Guardar SQL | `to_sql` | método | Guardar en base de datos | [ver](examples/escritura_sql__to_sql.py) |
| Guardar HTML | `to_html` | método | Exportar como tabla HTML | [ver](examples/escritura_html__to_html.py) |

---

## Exploración de Datos

### Inspección básica

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Primeras filas | `head` | método | Ver primeras N filas | [ver](examples/exploracion_primeras_filas__head.py) |
| Últimas filas | `tail` | método | Ver últimas N filas | [ver](examples/exploracion_ultimas_filas__tail.py) |
| Información general | `info` | método | Tipo y no-nulos de columnas | [ver](examples/exploracion_info__info.py) |
| Descripción estadística | `describe` | método | Estadísticas básicas | [ver](examples/exploracion_describe__describe.py) |
| Forma del dataset | `shape` | atributo | Filas y columnas | [ver](examples/exploracion_forma__shape.py) |
| Nombres de columnas | `columns` | atributo | Índice de columnas | [ver](examples/exploracion_columnas__columns.py) |
| Tipos de datos | `dtypes` | atributo | Tipo de cada columna | [ver](examples/exploracion_dtypes__dtypes.py) |
| Valores únicos | `unique` | método | Valores diferentes en columna | [ver](examples/exploracion_unicos__unique.py) |
| Conteo de valores | `value_counts` | método | Frecuencia de valores | [ver](examples/exploracion_value_counts__value_counts.py) |
| Información nulos | `isnull` | método | Detectar valores nulos | [ver](examples/exploracion_isnull__isnull.py) |

---

## Selección y Acceso a Datos

### Indexación y selección

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Seleccionar columna | `[]` | operador | Acceder a una columna | [ver](examples/seleccion_columna__bracket.py) |
| Seleccionar filas por label | `loc` | método | Acceso por etiqueta | [ver](examples/seleccion_loc__loc.py) |
| Seleccionar filas por posición | `iloc` | método | Acceso por posición | [ver](examples/seleccion_iloc__iloc.py) |
| Seleccionar con condición | `query` | método | Filtrar con expresión | [ver](examples/seleccion_query__query.py) |
| Filtro booleano | `[]` | operador | Filtrar con máscara booleana | [ver](examples/seleccion_boolean__boolean.py) |
| Seleccionar por tipo | `select_dtypes` | método | Columnas por tipo de dato | [ver](examples/seleccion_tipo__select_dtypes.py) |
| Acceder a valores | `at` | método | Acceso a un valor (label) | [ver](examples/seleccion_at__at.py) |
| Acceder posición | `iat` | método | Acceso a un valor (posición) | [ver](examples/seleccion_iat__iat.py) |

---

## Limpieza y Preparación

### Manejo de valores faltantes

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Eliminar nulos | `dropna` | método | Quitar filas con nulos | [ver](examples/limpieza_dropna__dropna.py) |
| Rellenar nulos | `fillna` | método | Completar valores faltantes | [ver](examples/limpieza_fillna__fillna.py) |
| Interpolar | `interpolate` | método | Interpolar valores faltantes | [ver](examples/limpieza_interpolate__interpolate.py) |
| Detectar nulos | `isna` | método | Máscara de valores nulos | [ver](examples/limpieza_isna__isna.py) |
| Contar nulos | `isnull` | método | Contar valores nulos | [ver](examples/limpieza_notna__notna.py) |

### Duplicados y tipos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Detectar duplicados | `duplicated` | método | Identificar filas repetidas | [ver](examples/limpieza_duplicated__duplicated.py) |
| Eliminar duplicados | `drop_duplicates` | método | Quitar filas repetidas | [ver](examples/limpieza_drop_duplicates__drop_duplicates.py) |
| Cambiar tipo de dato | `astype` | método | Convertir tipo de columna | [ver](examples/limpieza_astype__astype.py) |
| Renombrar columnas | `rename` | método | Cambiar nombres de columnas | [ver](examples/limpieza_rename__rename.py) |
| Eliminar columnas | `drop` | método | Quitar columnas o filas | [ver](examples/limpieza_drop__drop.py) |

---

## Transformación de Datos

### Operaciones con strings

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Métodos string | `.str` | accessor | Operaciones de texto | [ver](examples/transformacion_str__str_methods.py) |
| Convertir a mayúsculas | `.str.upper` | método | Convertir a MAYÚSCULAS | [ver](examples/transformacion_upper__upper.py) |
| Convertir a minúsculas | `.str.lower` | método | Convertir a minúsculas | [ver](examples/transformacion_lower__lower.py) |
| Longitud de string | `.str.len` | método | Largo de texto en columna | [ver](examples/transformacion_len__len.py) |
| Dividir strings | `.str.split` | método | Separar texto por delimitador | [ver](examples/transformacion_split__split.py) |
| Reemplazar texto | `.str.replace` | método | Cambiar texto | [ver](examples/transformacion_replace__replace.py) |
| Contiene patrón | `.str.contains` | método | Buscar patrón en texto | [ver](examples/transformacion_contains__contains.py) |

### Aplicar funciones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Aplicar función | `apply` | método | Ejecutar función en datos | [ver](examples/transformacion_apply__apply.py) |
| Mapear valores | `map` | método | Transformar valores de serie | [ver](examples/transformacion_map__map.py) |
| Aplicar por fila | `apply(axis=1)` | método | Aplicar función a cada fila | [ver](examples/transformacion_apply_fila__apply_row.py) |

### Operaciones aritméticas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Suma | `+` | operador | Sumar columnas | [ver](examples/transformacion_suma__sum_op.py) |
| Resta | `-` | operador | Restar columnas | [ver](examples/transformacion_resta__sub_op.py) |
| Multiplicación | `*` | operador | Multiplicar columnas | [ver](examples/transformacion_multiplicacion__mult_op.py) |
| División | `/` | operador | Dividir columnas | [ver](examples/transformacion_division__div_op.py) |

---

## Agregación y Estadísticas

### Funciones de agregación

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Suma | `sum` | método | Sumar valores | [ver](examples/agregacion_suma__sum.py) |
| Promedio | `mean` | método | Promedio de valores | [ver](examples/agregacion_promedio__mean.py) |
| Mediana | `median` | método | Valor central | [ver](examples/agregacion_mediana__median.py) |
| Moda | `mode` | método | Valor más frecuente | [ver](examples/agregacion_moda__mode.py) |
| Desviación estándar | `std` | método | Desviación estándar | [ver](examples/agregacion_desv_std__std.py) |
| Varianza | `var` | método | Varianza de datos | [ver](examples/agregacion_varianza__var.py) |
| Mínimo | `min` | método | Valor mínimo | [ver](examples/agregacion_minimo__min.py) |
| Máximo | `max` | método | Valor máximo | [ver](examples/agregacion_maximo__max.py) |
| Cuantil | `quantile` | método | Percentiles | [ver](examples/agregacion_cuantil__quantile.py) |
| Contar | `count` | método | Número de no-nulos | [ver](examples/agregacion_contar__count.py) |

### Agrupación

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Agrupar | `groupby` | método | Agrupar por columna | [ver](examples/agregacion_groupby__groupby.py) |
| Agregación múltiple | `agg` | método | Aplicar múltiples funciones | [ver](examples/agregacion_agg__agg.py) |
| Suma por grupo | `groupby().sum` | método | Suma por grupo | [ver](examples/agregacion_groupby_sum__groupby_sum.py) |
| Promedio por grupo | `groupby().mean` | método | Promedio por grupo | [ver](examples/agregacion_groupby_mean__groupby_mean.py) |
| Tamaño de grupos | `groupby().size` | método | Contar elementos por grupo | [ver](examples/agregacion_groupby_size__groupby_size.py) |
| Transformar grupos | `groupby().transform` | método | Aplicar función dentro de grupos | [ver](examples/agregacion_groupby_transform__groupby_transform.py) |

---

## Combinación de DataFrames

### Merge y Join

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Merge (inner) | `merge` | función | Combinar por columna común | [ver](examples/combinacion_merge_inner__merge_inner.py) |
| Merge (left) | `merge(how='left')` | función | Mantener filas izquierda | [ver](examples/combinacion_merge_left__merge_left.py) |
| Merge (outer) | `merge(how='outer')` | función | Todas las filas | [ver](examples/combinacion_merge_outer__merge_outer.py) |
| Join | `join` | método | Combinar por índice | [ver](examples/combinacion_join__join.py) |
| Concatenar | `concat` | función | Apilar DataFrames | [ver](examples/combinacion_concat__concat.py) |
| Append | `append` | método | Agregar filas | [ver](examples/combinacion_append__append.py) |

---

## Pivoting y Reshaping

### Cambiar estructura

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Pivot table | `pivot_table` | función | Crear tabla pivote | [ver](examples/reshape_pivot_table__pivot_table.py) |
| Pivot | `pivot` | método | Remodelar datos | [ver](examples/reshape_pivot__pivot.py) |
| Melt | `melt` | función | Desapilar columnas | [ver](examples/reshape_melt__melt.py) |
| Stack | `stack` | método | Apilar columnas | [ver](examples/reshape_stack__stack.py) |
| Unstack | `unstack` | método | Desapilar índice | [ver](examples/reshape_unstack__unstack.py) |
| Transpose | `T` | atributo | Transponer filas/columnas | [ver](examples/reshape_transpose__transpose.py) |

---

## Operaciones con Fechas

### Parsing y conversión

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Convertir a datetime | `to_datetime` | función | Parsear fechas | [ver](examples/fechas_to_datetime__to_datetime.py) |
| Componentes de fecha | `.dt` | accessor | Acceder a año, mes, día | [ver](examples/fechas_dt_accessor__dt_accessor.py) |
| Extraer año | `.dt.year` | método | Año de fecha | [ver](examples/fechas_year__year.py) |
| Extraer mes | `.dt.month` | método | Mes de fecha | [ver](examples/fechas_month__month.py) |
| Extraer día | `.dt.day` | método | Día de fecha | [ver](examples/fechas_day__day.py) |
| Día de semana | `.dt.dayofweek` | método | Día semana (0=lunes) | [ver](examples/fechas_dayofweek__dayofweek.py) |
| Nombre de mes | `.dt.month_name` | método | Nombre del mes | [ver](examples/fechas_month_name__month_name.py) |

### Muestreo temporal

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Resamplear | `resample` | método | Cambiar frecuencia temporal | [ver](examples/fechas_resample__resample.py) |
| Agrupar por rango | `pd.cut` | función | Crear bins de tiempo | [ver](examples/fechas_cut__cut.py) |

---

## Estadísticas Avanzadas

### Cálculos estadísticos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Correlación | `corr` | método | Correlación entre columnas | [ver](examples/estadistica_corr__corr.py) |
| Covarianza | `cov` | método | Covarianza entre variables | [ver](examples/estadistica_cov__cov.py) |
| Ranking | `rank` | método | Ordenamiento/ranking | [ver](examples/estadistica_rank__rank.py) |
| Diferencia | `diff` | método | Diferencias entre filas | [ver](examples/estadistica_diff__diff.py) |
| Pct_change | `pct_change` | método | Cambio porcentual | [ver](examples/estadistica_pct_change__pct_change.py) |
| Cumulative sum | `cumsum` | método | Suma acumulada | [ver](examples/estadistica_cumsum__cumsum.py) |
| Cumulative product | `cumprod` | método | Producto acumulado | [ver](examples/estadistica_cumprod__cumprod.py) |
| Rolling | `rolling` | método | Operaciones en ventana | [ver](examples/estadistica_rolling__rolling.py) |

---

## Índices

### Manipulación de índices

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Establecer índice | `set_index` | método | Usar columna como índice | [ver](examples/indices_set_index__set_index.py) |
| Resetear índice | `reset_index` | método | Convertir índice a columna | [ver](examples/indices_reset_index__reset_index.py) |
| Cambiar nombre índice | `rename_axis` | método | Renombrar el índice | [ver](examples/indices_rename_axis__rename_axis.py) |
| Reindexar | `reindex` | método | Cambiar orden/valores índice | [ver](examples/indices_reindex__reindex.py) |

---

## Utilidades

### Operaciones comunes

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Ordenar | `sort_values` | método | Ordenar por valores | [ver](examples/utilidades_sort_values__sort_values.py) |
| Ordenar índice | `sort_index` | método | Ordenar por índice | [ver](examples/utilidades_sort_index__sort_index.py) |
| Muestra aleatoria | `sample` | método | Seleccionar filas al azar | [ver](examples/utilidades_sample__sample.py) |
| Valores entre | `between` | método | Filtrar rango de valores | [ver](examples/utilidades_between__between.py) |
| Isin | `isin` | método | Valores en lista | [ver](examples/utilidades_isin__isin.py) |
| Donde | `where` | método | Condición booleana | [ver](examples/utilidades_where__where.py) |
| Mask | `mask` | método | Inverso de where | [ver](examples/utilidades_mask__mask.py) |

---

## Conjuntos de datos disponibles

Los ejemplos usan estos datasets en `datasets/`:

- **personas.csv**: Datos de empleados (id, nombre, edad, departamento, salario)
- **ventas.csv**: Registro de ventas (id_venta, id_empleado, id_producto, cantidad, fecha)
- **productos.csv**: Catálogo de productos (id, nombre, categoría, precio, stock)
- **calificaciones.csv**: Notas de estudiantes (id, nombre, calificaciones en distintas materias)
- **clima.csv**: Datos meteorológicos (fecha, ciudad, temperatura, humedad)
- **frutas.csv**: Inventario con valores faltantes (para ejemplos de limpieza)
