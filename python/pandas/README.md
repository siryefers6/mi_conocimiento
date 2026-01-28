# Pandas - Ejemplos de Operaciones Comunes

## Carga de datos

| Concepto                | Referencia  | Tipo     | Uso                        | Ejemplo |
|-------------------------|-------------|----------|----------------------------|---------|
| Leer CSV                | `read_csv`  | funcion  | Cargar archivo CSV         | [ver](examples/cargar_csv__read_csv.py) |
| Crear DataFrame manual  | `DataFrame` | clase    | Datos en memoria           | [ver](examples/crear_dataframe__DataFrame.py) |

---

## Inspección y exploración de datos

| Concepto                 | Referencia | Tipo    | Uso                                 | Ejemplo |
|--------------------------|------------|---------|-------------------------------------|---------|
| Ver primeras filas       | `head`     | metodo  | Inspección rápida inicial           | [ver](examples/inspeccionar_datos__head.py) |
| Ver últimas filas        | `tail`     | metodo  | Inspección final                    | [ver](examples/inspeccionar_datos__tail.py) |
| Tamaño del DataFrame     | `shape`    | atributo | Filas y columnas                    | [ver](examples/ver_dimension__shape.py) |
| Nombres de columnas      | `columns`  | atributo | Listar columnas                     | [ver](examples/ver_columnas__columns.py) |
| Información general      | `info`     | metodo  | Tipos de datos y nulos              | [ver](examples/analizar_estructura__info.py) |
| Estadísticas descriptivas | `describe` | metodo  | Resumen estadístico                 | [ver](examples/resumen_estadistico__describe.py) |
| Conteo por columna       | `count`    | metodo  | Valores no nulos                    | [ver](examples/conteo_valores__count.py) |
| Valores únicos           | `nunique`  | metodo  | Cardinalidad                        | [ver](examples/valores_unicos__nunique.py) |
| Frecuencia de valores    | `value_counts` | metodo | Distribución de categorías          | [ver](examples/frecuencia_valores__value_counts.py) |

---

## Selección y acceso a datos

| Concepto                     | Referencia | Tipo    | Uso                                 | Ejemplo |
|------------------------------|------------|---------|-------------------------------------|---------|
| Seleccionar columna          | `[]`       | sintaxis | Acceder a una columna               | [ver](examples/seleccionar_columna__brackets.py) |
| Seleccionar múltiples columnas | `[]`    | sintaxis | Acceder a varias columnas           | [ver](examples/seleccionar_columnas__brackets.py) |
| Selección por etiquetas      | `loc`      | metodo  | Filas y columnas por etiqueta       | [ver](examples/seleccionar_por_etiqueta__loc.py) |
| Selección por posición       | `iloc`     | metodo  | Filas y columnas por índice         | [ver](examples/seleccionar_por_posicion__iloc.py) |
| Selección condicional        | `loc`      | metodo  | Filtrar filas por condición         | [ver](examples/filtrar_por_condicion__loc.py) |
| Selección por fecha          | `loc`      | metodo  | Filtrar filas por rango de fechas   | [ver](examples/filtrar_por_fecha__loc.py) |
| Acceso a celda única         | `at`       | metodo  | Acceso rápido a un valor            | [ver](examples/acceso_celda__at.py) |
| Acceso por posición única    | `iat`      | metodo  | Acceso rápido por índice            | [ver](examples/acceso_posicion__iat.py) |
| Seleccionar filas aleatorias | `sample`   | metodo  | Muestreo aleatorio                  | [ver](examples/seleccionar_aleatorio__sample.py) |
| Filtrar columnas por nombre  | `filter`   | metodo  | Filtrar columnas por patrón         | [ver](examples/filtrar_columnas__filter.py) |

---

## Limpieza y preparación de datos

| Concepto                   | Referencia            | Tipo    | Uso                                 | Ejemplo |
|----------------------------|-----------------------|---------|-------------------------------------|---------|
| Detectar valores nulos     | `isna`                | metodo  | Identificar datos faltantes         | [ver](examples/detectar_nulos__isna.py) |
| Contar valores nulos       | `isna().sum()`        | metodo  | Cuantificar nulos por columna       | [ver](examples/contar_nulos__isna_sum.py) |
| Rellenar valores nulos     | `fillna`              | metodo  | Imputar valores faltantes           | [ver](examples/rellenar_nulos__fillna.py) |
| Eliminar filas con nulos   | `dropna`              | metodo  | Quitar filas incompletas            | [ver](examples/eliminar_filas_nulas__dropna.py) |
| Eliminar columnas vacías   | `dropna(axis=1)`      | metodo  | Quitar columnas incompletas         | [ver](examples/eliminar_columnas_nulas__dropna.py) |
| Eliminar duplicados        | `drop_duplicates`     | metodo  | Quitar registros repetidos          | [ver](examples/eliminar_duplicados__drop_duplicates.py) |
| Cambiar tipo de dato       | `astype`              | metodo  | Conversión explícita de tipos       | [ver](examples/cambiar_tipo__astype.py) |
| Convertir a datetime       | `to_datetime`         | funcion | Asegurar formato de fecha           | [ver](examples/convertir_fecha__to_datetime.py) |
| Extraer componentes fecha  | `dt`                  | propiedad | Día, mes, año, semana             | [ver](examples/extraer_componentes_fecha__dt.py) |
| Normalizar texto           | `str.lower().strip()`| metodo  | Limpiar y estandarizar strings      | [ver](examples/normalizar_texto__str.py) |
| Reemplazar texto           | `str.replace`         | metodo  | Reemplazar valores en texto         | [ver](examples/reemplazar_texto__str_replace.py) |
| Filtrar por patrón         | `str.contains`        | metodo  | Filtrar filas según patrón texto    | [ver](examples/extraer_patron__str_contains.py) |
| Reemplazar valores         | `replace`             | metodo  | Sustituir valores específicos       | [ver](examples/reemplazar_valores__replace.py) |

---

## Transformaciones y nuevas columnas

| Concepto                  | Referencia | Tipo     | Uso                                 | Ejemplo |
|---------------------------|------------|----------|-------------------------------------|---------|
| Crear columna nueva       | `[]`       | sintaxis | Añadir nueva columna calculada      | [ver](examples/crear_columna_nueva__asignment.py) |
| Aplicar función a columna | `apply`    | metodo   | Transformar valores de una columna  | [ver](examples/aplicar_funcion__apply.py) |
| Mapear valores            | `map`      | metodo   | Reemplazo según dict o función      | [ver](examples/mapear_valores__map.py) |
| Operaciones vectorizadas  | numpy      | libreria | Crear columnas derivadas con NumPy  | [ver](examples/operaciones_vectorizadas__numpy.py) |

---

## Combinación de DataFrames

| Concepto              | Referencia | Tipo    | Uso                              | Ejemplo |
|-----------------------|------------|---------|----------------------------------|---------|
| Merge / Join          | `merge`    | funcion | Combinar según columna clave     | [ver](examples/merge_dataframes__merge.py) |
| Concatenar DataFrames | `concat`   | funcion | Unir filas o columnas            | [ver](examples/concatenar_dataframes__concat.py) |

---

## Agrupaciones y agregaciones

| Concepto               | Referencia       | Tipo   | Uso                                | Ejemplo |
|------------------------|------------------|--------|-------------------------------------|---------|
| Agrupar por columna    | `groupby`        | metodo | Agrupar datos para agregación      | [ver](examples/agrupar_por_columna__groupby.py) |
| Agregaciones básicas   | `groupby().agg()`| metodo | Calcular métricas sobre grupos     | [ver](examples/agregaciones_basicas__groupby.py) |
| Estadísticas por grupo | `groupby().agg()`| metodo | Múltiples estadísticas por grupo   | [ver](examples/obtener_estadisticas_grupo__agg.py) |
| Contar valores por grupo | `value_counts` | metodo | Frecuencia de valores              | [ver](examples/contar_por_grupo__value_counts.py) |

---

## Ordenamiento

| Concepto             | Referencia   | Tipo   | Uso                              | Ejemplo |
|----------------------|--------------|--------|----------------------------------|---------|
| Ordenar por columna  | `sort_values`| metodo | Ordenar filas según columna      | [ver](examples/ordenar_datos__sort_values.py) |

---

## Análisis estadístico

| Concepto              | Referencia    | Tipo     | Uso                                       | Ejemplo |
|-----------------------|---------------|----------|-------------------------------------------|---------|
| Matriz de correlación | `corr`        | metodo   | Medir relación entre variables numéricas  | [ver](examples/matriz_correlacion__corr.py) |
| Tabla pivote          | `pivot_table` | funcion  | Resumir datos en tabla cruzada            | [ver](examples/pivote_tabla__pivot_table.py) |

---

## Datasets disponibles

- **ventas.csv**: 20 registros con información de ventas (fecha, producto, categoría, precio, stock, cliente)
- **clientes.csv**: 17 clientes con datos demográficos (nombre, email, ciudad, país, estado civil, ingresos)
- **productos.csv**: 14 productos con información de catálogo (nombre, categoría, precios, proveedor)
- **transacciones.csv**: 20 transacciones con estados de pago y métodos de pago
