## Carga de datos

| Concepto                  | Referencia       | Tipo     | Uso                                      | Ejemplo                                          |
|---------------------------|------------------|----------|------------------------------------------|--------------------------------------------------|
| Leer CSV                  | `read_csv`       | funcion  | Cargar archivo CSV                       | [ver](examples/cargar_csv__read_csv.py)          |
| Leer CSV con separador    | `read_csv`       | funcion  | Separador personalizado                  | [ver](examples/cargar_csv_sep__read_csv.py)      |
| Leer CSV con tipos        | `read_csv`       | funcion  | Definir dtypes                           | [ver](examples/cargar_csv_tipos__read_csv.py)    |
| Leer CSV con fechas       | `read_csv`       | funcion  | Parsear fechas                           | [ver](examples/cargar_csv_fechas__read_csv.py)   |
| Leer CSV con nulos        | `read_csv`       | funcion  | Definir valores nulos                    | [ver](examples/cargar_csv_nulos__read_csv.py)    |
| Crear DataFrame manual    | `DataFrame`      | clase    | Datos en memoria                         | [ver](examples/crear_dataframe__DataFrame.py)    |

---

## Inspección y exploración de datos

| Concepto                | Referencia | Tipo   | Uso                                     | Ejemplo                                         |
|-------------------------|------------|--------|-----------------------------------------|-------------------------------------------------|
| Ver primeras filas      | `head`     | metodo | Inspección rápida inicial               | [ver](examples/inspeccionar_datos__head.py)     |
| Ver últimas filas       | `tail`     | metodo | Inspección final                        | [ver](examples/inspeccionar_datos__tail.py)     |
| Tamaño del DataFrame    | `shape`    | atributo | Filas y columnas                        | [ver](examples/ver_dimension__shape.py)         |
| Nombres de columnas     | `columns`  | atributo | Listar columnas                         | [ver](examples/ver_columnas__columns.py)        |
| Información general     | `info`     | metodo | Tipos de datos y nulos                  | [ver](examples/analizar_estructura__info.py)    |
| Estadísticas descriptivas | `describe` | metodo | Resumen estadístico                     | [ver](examples/resumen_estadistico__describe.py)|
| Conteo por columna      | `count`    | metodo | Valores no nulos                        | [ver](examples/conteo_valores__count.py)        |
| Valores únicos          | `nunique`  | metodo | Cardinalidad                            | [ver](examples/valores_unicos__nunique.py)      |
| Frecuencia de valores   | `value_counts` | metodo | Distribución de categorías             | [ver](examples/frecuencia_valores__value_counts.py) |

---

## Selección y acceso a datos

| Concepto                     | Referencia        | Tipo     | Uso                                              | Ejemplo                                              |
|------------------------------|-------------------|----------|--------------------------------------------------|------------------------------------------------------|
| Seleccionar columna          | `[]`              | sintaxis | Acceder a una columna                            | [ver](examples/seleccionar_columna__brackets.py)     |
| Seleccionar múltiples columnas | `[]`            | sintaxis | Acceder a varias columnas                        | [ver](examples/seleccionar_columnas__brackets.py)    |
| Selección por etiquetas      | `loc`             | metodo   | Filas y columnas por etiqueta                    | [ver](examples/seleccionar_por_etiqueta__loc.py)     |
| Selección por posición       | `iloc`            | metodo   | Filas y columnas por índice                      | [ver](examples/seleccionar_por_posicion__iloc.py)    |
| Selección condicional        | `loc`             | metodo   | Filtrar filas por condición                      | [ver](examples/filtrar_por_condicion__loc.py)        |
| Acceso a celda única         | `at`              | metodo   | Acceso rápido a un valor                         | [ver](examples/acceso_celda__at.py)                  |
| Acceso por posición única    | `iat`             | metodo   | Acceso rápido por índice                         | [ver](examples/acceso_posicion__iat.py)              |
| Seleccionar filas aleatorias | `sample`          | metodo   | Muestreo aleatorio                               | [ver](examples/seleccionar_aleatorio__sample.py)     |
| Limitar columnas visibles    | `filter`          | metodo   | Filtrar columnas por nombre                      | [ver](examples/filtrar_columnas__filter.py)          |

---

## Limpieza y preparación de datos

| Concepto                         | Referencia           | Tipo     | Uso                                                | Ejemplo                                               |
|----------------------------------|----------------------|----------|----------------------------------------------------|-------------------------------------------------------|
| Detectar valores nulos           | `isna / isnull`      | metodo   | Identificar datos faltantes                        | [ver](examples/detectar_nulos__isna.py)              |
| Contar valores nulos             | `isna().sum()`       | metodo   | Cuantificar nulos por columna                      | [ver](examples/contar_nulos__isna_sum.py)            |
| Eliminar filas con nulos         | `dropna`             | metodo   | Quitar filas incompletas                           | [ver](examples/eliminar_filas_nulas__dropna.py)      |
| Eliminar columnas con nulos      | `dropna(axis=1)`     | metodo   | Quitar columnas incompletas                        | [ver](examples/eliminar_columnas_nulas__dropna.py)   |
| Rellenar valores nulos           | `fillna`             | metodo   | Imputar valores faltantes                          | [ver](examples/rellenar_nulos__fillna.py)            |
| Reemplazar valores               | `replace`            | metodo   | Sustituir valores específicos                      | [ver](examples/reemplazar_valores__replace.py)       |
| Cambiar tipo de dato             | `astype`             | metodo   | Conversión explícita de tipos                      | [ver](examples/cambiar_tipo__astype.py)              |
| Normalizar texto                 | `str.lower`          | metodo   | Normaliza texto a minúsculas                       | [ver](examples/normalizar_texto__str_lower.py)       |
| Eliminar espacios en blanco      | `str.strip`          | metodo   | Limpieza de strings                                | [ver](examples/normalizar_texto__str_strip.py)       |
| Filtrar por patrón               | `str.contains`       | metodo   | Filtrar filas según texto o patrón                 | [ver](examples/extraer_patron__str_contains.py) |
| Reemplazar texto                 | `str.replace`        | metodo   | Reemplazar valores o patrones en texto             | [ver](examples/reemplazar_texto__str_replace.py) |
| Renombrar columnas               | `rename`             | metodo   | Estandarizar nombres                               | [ver](examples/renombrar_columnas__rename.py)        |
| Eliminar duplicados              | `drop_duplicates`    | metodo   | Quitar registros repetidos                         | [ver](examples/eliminar_duplicados__drop_duplicates.py) |

---

## Transformaciones y nuevas columnas

| Concepto                  | Referencia | Tipo     | Uso                                             | Ejemplo                                                 |
| ------------------------- | ---------- | -------- | ----------------------------------------------- | ------------------------------------------------------- |
| Crear columna             | `[]`       | sintaxis | Añadir nueva columna                            | [ver](examples/crear_columna__brackets.py)              |
| Aplicar función a columna | `apply`    | metodo   | Transformar valores de una columna              | [ver](examples/aplicar_funcion__apply.py)               |
| Mapear valores            | `map`      | metodo   | Reemplazo o transformación según dict o función | [ver](examples/mapear_valores__map.py)                  |
| Operaciones vectorizadas  | `+,-,*,/`  | operador | Crear columnas derivadas mediante cálculos      | [ver](examples/operaciones_vectorizadas__operadores.py) |

---

## Agrupaciones y agregaciones

| Concepto               | Referencia               | Tipo   | Uso                               | Ejemplo                                              |
| ---------------------- | ------------------------ | ------ | --------------------------------- | ---------------------------------------------------- |
| Agrupar por columna    | `groupby`                | metodo | Agrupar datos para agregación     | [ver](examples/agrupar_por_columna__groupby.py)      |
| Agregaciones básicas   | `sum,mean,min,max,count` | metodo | Calcular métricas sobre grupos    | [ver](examples/agregaciones_basicas__groupby_agg.py) |
| Agregaciones múltiples | `agg`                    | metodo | Aplicar varias funciones a la vez | [ver](examples/agregaciones_multiples__agg.py)       |

---

## Ordenamiento

| Concepto            | Referencia    | Tipo   | Uso                         | Ejemplo                                             |
| ------------------- | ------------- | ------ | --------------------------- | --------------------------------------------------- |
| Ordenar por columna | `sort_values` | metodo | Ordenar filas según columna | [ver](examples/ordenar_por_columna__sort_values.py) |
| Ordenar por índice  | `sort_index`  | metodo | Ordenar por índice          | [ver](examples/ordenar_por_indice__sort_index.py)   |

---

## Combinación de DataFrames

| Concepto              | Referencia | Tipo    | Uso                          | Ejemplo                                          |
| --------------------- | ---------- | ------- | ---------------------------- | ------------------------------------------------ |
| Concatenar DataFrames | `concat`   | funcion | Unir filas o columnas        | [ver](examples/concatenar_dataframes__concat.py) |
| Merge / Join          | `merge`    | metodo  | Combinar según columna clave | [ver](examples/merge_dataframes__merge.py)       |
| Unir índices          | `join`     | metodo  | Unir DataFrames por índice   | [ver](examples/join_dataframes__join.py)         |

---

## Fechas y tiempos

| Concepto                     | Referencia      | Tipo     | Uso                        | Ejemplo                                          |
| ---------------------------- | --------------- | -------- | -------------------------- | ------------------------------------------------ |
| Convertir a datetime         | `to_datetime`   | funcion  | Asegurar formato de fecha  | [ver](examples/convertir_fecha__to_datetime.py)  |
| Extraer componentes de fecha | `dt`            | atributo | Día, mes, año, semana      | [ver](examples/extraer_componentes_fecha__dt.py) |
| Filtrar por fecha            | `loc` / `query` | metodo   | Seleccionar rango temporal | [ver](examples/filtrar_por_fecha__loc.py)        |

---

## Estadísticas y resúmenes avanzados

| Concepto                 | Referencia                 | Tipo   | Uso                                      | Ejemplo                                                   |
| ------------------------ | -------------------------- | ------ | ---------------------------------------- | --------------------------------------------------------- |
| Correlación              | `corr`                     | metodo | Medir relación entre variables numéricas | [ver](examples/correlacion__corr.py)                      |
| Covarianza               | `cov`                      | metodo | Relación de dispersión conjunta          | [ver](examples/covarianza__cov.py)                        |
| Contar valores por grupo | `value_counts` + `groupby` | metodo | Frecuencia por categoría                 | [ver](examples/contar_por_grupo__value_counts_groupby.py) |

---
