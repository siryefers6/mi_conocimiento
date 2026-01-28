# Microsoft Access SQL - Referencia Completa

Referencia rápida de sentencias, funciones y conceptos de SQL en Microsoft Access con ejemplos ejecutables basados en un dataset real.

**⚠️ IMPORTANTE:** Todos los ejemplos están basados en el dataset documentado en [DATASET.md](DATASET.md). Consulta ese archivo para entender la estructura de datos utilizada en los ejemplos.

---

## Dataset de Ejemplo

Este repositorio utiliza un dataset realista con 3 tablas relacionadas:
- **Empleados**: Información de empleados con salarios y fechas
- **Departamentos**: Departamentos de la empresa con presupuestos
- **Proyectos**: Proyectos activos y completados

Ver [DATASET.md](DATASET.md) para la estructura completa y datos de ejemplo.

---

## DDL - Definición de Datos

### Crear y Eliminar

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear tabla | `CREATE TABLE` | DDL | Definir nueva tabla | [ver](examples/crear_tabla__CREATE_TABLE.sql) |
| Eliminar tabla | `DROP TABLE` | DDL | Borrar tabla | [ver](examples/eliminar_tabla__DROP_TABLE.sql) |
| Crear índice | `CREATE INDEX` | DDL | Optimizar búsquedas | [ver](examples/crear_indice__CREATE_INDEX.sql) |
| Crear vista (query) | `CREATE VIEW` | DDL | Consulta guardada | [ver](examples/crear_vista__CREATE_VIEW.sql) |

### Modificar Estructura

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Modificar tabla | `ALTER TABLE` | DDL | Cambiar estructura | [ver](examples/modificar_tabla__ALTER_TABLE.sql) |
| Agregar columna | `ADD COLUMN` | DDL | Añadir campo | [ver](examples/agregar_columna__ADD_COLUMN.sql) |
| Eliminar columna | `DROP COLUMN` | DDL | Borrar campo | [ver](examples/eliminar_columna__DROP_COLUMN.sql) |
| Renombrar columna | `RENAME COLUMN` | DDL | Cambiar nombre campo | [ver](examples/renombrar_columna__RENAME_COLUMN.sql) |
| Cambiar tipo columna | `ALTER COLUMN TYPE` | DDL | Modificar tipo datos | [ver](examples/cambiar_tipo_columna__ALTER_COLUMN_TYPE.sql) |

### Restricciones

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Clave primaria | `PRIMARY KEY` | constraint | Identificador único | [ver](examples/clave_primaria__PRIMARY_KEY.sql) |
| Clave foránea | `FOREIGN KEY` | constraint | Relación entre tablas | [ver](examples/clave_foranea__FOREIGN_KEY.sql) |
| Restricción UNIQUE | `UNIQUE` | constraint | Valores únicos | [ver](examples/restriccion_unique__UNIQUE.sql) |
| Restricción NOT NULL | `NOT NULL` | constraint | Campo obligatorio | [ver](examples/restriccion_not_null__NOT_NULL.sql) |
| Restricción CHECK | `CHECK` | constraint | Validación de valor | [ver](examples/restriccion_check__CHECK.sql) |
| Valor por defecto | `DEFAULT` | constraint | Valor predeterminado | [ver](examples/valor_por_defecto__DEFAULT.sql) |

---

## DML - Manipulación de Datos

### Inserción

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Insertar fila | `INSERT INTO` | DML | Añadir registro | [ver](examples/insertar_fila__INSERT_INTO.sql) |
| Insertar múltiples filas | `INSERT INTO VALUES` | DML | Añadir varios registros | [ver](examples/insertar_multiples__INSERT_MULTIPLE.sql) |
| Insertar desde SELECT | `INSERT INTO SELECT` | DML | Copiar datos | [ver](examples/insertar_desde_select__INSERT_SELECT.sql) |

### Actualización

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Actualizar registros | `UPDATE` | DML | Modificar datos | [ver](examples/actualizar_registros__UPDATE.sql) |
| UPDATE con WHERE | `UPDATE WHERE` | DML | Actualizar condicionalmente | [ver](examples/actualizar_con_where__UPDATE_WHERE.sql) |
| UPDATE con JOIN | `UPDATE FROM` | DML | Actualizar con relación | [ver](examples/actualizar_con_join__UPDATE_JOIN.sql) |

### Eliminación

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Eliminar registros | `DELETE` | DML | Borrar datos | [ver](examples/eliminar_registros__DELETE.sql) |
| DELETE con WHERE | `DELETE WHERE` | DML | Eliminar condicionalmente | [ver](examples/eliminar_con_where__DELETE_WHERE.sql) |

---

## DQL - Consultas (SELECT)

### SELECT Básico

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Seleccionar todas columnas | `SELECT *` | DQL | Obtener todos campos | [ver](examples/seleccionar_todos__SELECT_STAR.sql) |
| Seleccionar columnas específicas | `SELECT col1, col2` | DQL | Obtener campos seleccionados | [ver](examples/seleccionar_columnas__SELECT_COLS.sql) |
| Alias de columna | `AS` | DQL | Renombrar en resultado | [ver](examples/alias_columna__AS.sql) |
| DISTINCT | `DISTINCT` | DQL | Eliminar duplicados | [ver](examples/eliminar_duplicados__DISTINCT.sql) |
| TOP | `TOP` | DQL | Limitar resultados | [ver](examples/limitar_resultados__TOP.sql) |

### Filtrado

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Filtrar con WHERE | `WHERE` | DQL | Condición simple | [ver](examples/filtrar_where__WHERE.sql) |
| AND lógico | `AND` | DQL | Múltiples condiciones | [ver](examples/operador_and__AND.sql) |
| OR lógico | `OR` | DQL | Alternativas | [ver](examples/operador_or__OR.sql) |
| IN | `IN` | DQL | Valores en lista | [ver](examples/operador_in__IN.sql) |
| BETWEEN | `BETWEEN` | DQL | Rango de valores | [ver](examples/operador_between__BETWEEN.sql) |
| LIKE | `LIKE` | DQL | Búsqueda por patrón | [ver](examples/operador_like__LIKE.sql) |
| IS NULL | `IS NULL` | DQL | Valores nulos | [ver](examples/verificar_nulo__IS_NULL.sql) |

### Ordenamiento y Agrupación

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Ordenar ascendente | `ORDER BY ASC` | DQL | Ordenar A-Z | [ver](examples/ordenar_asc__ORDER_BY_ASC.sql) |
| Ordenar descendente | `ORDER BY DESC` | DQL | Ordenar Z-A | [ver](examples/ordenar_desc__ORDER_BY_DESC.sql) |
| Agrupar registros | `GROUP BY` | DQL | Agrupar datos | [ver](examples/agrupar_datos__GROUP_BY.sql) |
| Filtrar grupos | `HAVING` | DQL | Condición en grupos | [ver](examples/filtrar_grupos__HAVING.sql) |

### Funciones de Agregación

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Contar registros | `COUNT()` | función | Cantidad de filas | [ver](examples/contar_registros__COUNT.sql) |
| Suma | `SUM()` | función | Sumar valores | [ver](examples/sumar_valores__SUM.sql) |
| Promedio | `AVG()` | función | Media aritmética | [ver](examples/promedio_valores__AVG.sql) |
| Máximo | `MAX()` | función | Valor mayor | [ver](examples/valor_maximo__MAX.sql) |
| Mínimo | `MIN()` | función | Valor menor | [ver](examples/valor_minimo__MIN.sql) |

### JOINs

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| INNER JOIN | `INNER JOIN` | DQL | Intersección de tablas | [ver](examples/inner_join__INNER_JOIN.sql) |
| LEFT JOIN | `LEFT JOIN` | DQL | Tabla izquierda + coincidencias | [ver](examples/left_join__LEFT_JOIN.sql) |
| RIGHT JOIN | `RIGHT JOIN` | DQL | Tabla derecha + coincidencias | [ver](examples/right_join__RIGHT_JOIN.sql) |
| FULL JOIN | `FULL OUTER JOIN` | DQL | Todas las filas | [ver](examples/full_join__FULL_OUTER_JOIN.sql) |
| CROSS JOIN | `CROSS JOIN` | DQL | Producto cartesiano | [ver](examples/cross_join__CROSS_JOIN.sql) |
| SELF JOIN | `JOIN a sí misma` | DQL | Tabla con ella misma | [ver](examples/self_join__SELF_JOIN.sql) |

### Subconsultas

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Subconsulta en WHERE | `SELECT (SELECT)` | DQL | Consulta anidada | [ver](examples/subconsulta_where__SUBQUERY_WHERE.sql) |
| Subconsulta en FROM | `FROM (SELECT)` | DQL | Tabla derivada | [ver](examples/subconsulta_from__SUBQUERY_FROM.sql) |
| EXISTS | `EXISTS` | DQL | Verificar existencia | [ver](examples/verificar_existe__EXISTS.sql) |

### Operaciones de Conjuntos

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| UNION | `UNION` | DQL | Combinación sin duplicados | [ver](examples/union__UNION.sql) |
| UNION ALL | `UNION ALL` | DQL | Combinación con duplicados | [ver](examples/union_all__UNION_ALL.sql) |

---

## Funciones y Expresiones

### Funciones de Texto

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Concatenar | `&` o `+` | función | Unir strings | [ver](examples/concatenar_strings__CONCAT.sql) |
| Mayúsculas | `UCASE()` | función | Convertir a mayúsculas | [ver](examples/convertir_mayusculas__UCASE.sql) |
| Minúsculas | `LCASE()` | función | Convertir a minúsculas | [ver](examples/convertir_minusculas__LCASE.sql) |
| Largo | `LEN()` | función | Longitud de string | [ver](examples/longitud_string__LEN.sql) |
| Subcadena | `MID()` | función | Extraer parte | [ver](examples/extraer_subcadena__MID.sql) |
| Remover espacios | `TRIM()` | función | Eliminar espacios | [ver](examples/remover_espacios__TRIM.sql) |
| Reemplazar | `REPLACE()` | función | Sustituir texto | [ver](examples/reemplazar_texto__REPLACE.sql) |

### Funciones Numéricas

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Valor absoluto | `ABS()` | función | Número sin signo | [ver](examples/valor_absoluto__ABS.sql) |
| Redondear | `ROUND()` | función | Redondear número | [ver](examples/redondear__ROUND.sql) |
| Piso | `INT()` | función | Redondear hacia abajo | [ver](examples/piso__INT.sql) |
| Raíz cuadrada | `SQR()` | función | Calcular raíz | [ver](examples/raiz_cuadrada__SQR.sql) |
| Potencia | `^` | función | Elevar a potencia | [ver](examples/potencia__POWER.sql) |
| Módulo | `MOD` | función | Resto de división | [ver](examples/modulo__MOD.sql) |

### Funciones de Fecha

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Fecha actual | `DATE()` | función | Obtener hoy | [ver](examples/fecha_actual__DATE.sql) |
| Tiempo actual | `TIME()` | función | Obtener hora actual | [ver](examples/tiempo_actual__TIME.sql) |
| Fecha y hora | `NOW()` | función | Obtener ahora | [ver](examples/fecha_hora_actual__NOW.sql) |
| Extraer parte | `YEAR()`, `MONTH()`, `DAY()` | función | Obtener día/mes/año | [ver](examples/extraer_fecha__EXTRACT.sql) |
| Diferencia fechas | `DATEDIFF()` | función | Días entre fechas | [ver](examples/diferencia_fechas__DATEDIFF.sql) |
| Sumar días | `DATEADD()` | función | Agregar días | [ver](examples/sumar_dias__DATEADD.sql) |
| Formato fecha | `FORMAT()` | función | Formatear fecha | [ver](examples/formato_fecha__FORMAT.sql) |

### Funciones Condicionales

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| IIF | `IIF()` | función | Condicional simple | [ver](examples/iif__IIF.sql) |
| SWITCH | `SWITCH()` | función | Condicional múltiple | [ver](examples/switch__SWITCH.sql) |
| NZ | `NZ()` | función | Primer no nulo | [ver](examples/primer_no_nulo__NZ.sql) |

---

## Transacciones y Control

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Iniciar transacción | `BEGIN TRANSACTION` | control | Comenzar operación | [ver](examples/iniciar_transaccion__BEGIN.sql) |
| Confirmar cambios | `COMMIT` | control | Guardar cambios | [ver](examples/confirmar_cambios__COMMIT.sql) |
| Deshacer cambios | `ROLLBACK` | control | Revertir cambios | [ver](examples/deshacer_cambios__ROLLBACK.sql) |

---

## Seguridad y Permisos

Access maneja permisos a través de la interfaz, no directamente en SQL.

---

## Índices y Optimización

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Índice simple | `CREATE INDEX` | optimización | Índice básico | [ver](examples/indice_simple__CREATE_INDEX.sql) |
| Índice único | `UNIQUE INDEX` | optimización | Índice con unicidad | [ver](examples/indice_unico__UNIQUE_INDEX.sql) |
| Índice compuesto | `COMPOSITE INDEX` | optimización | Múltiples columnas | [ver](examples/indice_compuesto__COMPOSITE_INDEX.sql) |
| Eliminar índice | `DROP INDEX` | optimización | Borrar índice | [ver](examples/eliminar_indice__DROP_INDEX.sql) |

---

## Vistas y Tablas Derivadas

| Concepto | Sentencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Vista simple | `CREATE VIEW` | vista | Consulta guardada | [ver](examples/vista_simple__CREATE_VIEW.sql) |
| Vista con filtro | `VIEW WHERE` | vista | Vista filtrada | [ver](examples/vista_filtrada__VIEW_WHERE.sql) |
| Tabla derivada | `(SELECT)` | tabla | Tabla temporal | [ver](examples/tabla_derivada__DERIVED_TABLE.sql) |
| CTE (WITH) | `WITH` | CTE | Consulta con nombre | [ver](examples/cte_basica__WITH.sql) |
