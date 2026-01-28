# Índice de Recursos - SQL Access

## 📚 Documentación Principal

| Archivo | Descripción |
|---------|-------------|
| [DATASET.md](DATASET.md) | **Estructura del dataset** - Tablas, campos y datos de ejemplo |
| [GUIA_MEJORAS.md](GUIA_MEJORAS.md) | **Guía de cambios** - Qué se mejoró y cómo usar |
| [CAMBIOS_REALIZADOS.txt](CAMBIOS_REALIZADOS.txt) | **Resumen ejecutivo** - Lista completa de cambios |
| [README.md](README.md) | **Referencia completa** - Todos los conceptos y ejemplos |

---

## 🗂️ Estructura de Carpetas

```
sql/access/
├── README.md                    # Índice de conceptos SQL
├── DATASET.md                   # Dataset de ejemplo
├── GUIA_MEJORAS.md             # Guía de uso
├── CAMBIOS_REALIZADOS.txt      # Resumen de cambios
├── INDEX.md                     # Este archivo
├── dataset.json                 # Dataset en formato JSON
├── setup_db.py                  # Script de configuración
└── examples/                    # 110+ ejemplos SQL
    ├── crear_tabla__CREATE_TABLE.sql
    ├── insertar_fila__INSERT_INTO.sql
    ├── filtrar_where__WHERE.sql
    ├── inner_join__INNER_JOIN.sql
    ├── operador_and__AND.sql
    ├── operador_or__OR.sql
    ├── contar_registros__COUNT.sql
    ├── agrupar_datos__GROUP_BY.sql
    ├── ...
    └── ... (muchos más)
```

---

## 🎯 Cómo Empezar

### 1️⃣ Para Entender el Dataset
Abre: **[DATASET.md](DATASET.md)**
- Estructura de las 3 tablas
- Registros de ejemplo
- Scripts SQL para crear tablas

### 2️⃣ Para Ver qué Cambió
Abre: **[GUIA_MEJORAS.md](GUIA_MEJORAS.md)**
- Cambios realizados
- Ejemplos actualizados
- Cómo ejecutar

### 3️⃣ Para Aprender SQL
Abre: **[README.md](README.md)**
- DDL (Crear tablas)
- DML (Insertar, actualizar, eliminar)
- SELECT (Consultas)
- JOINS (Uniones)
- Funciones de agregación
- Operadores y funciones

### 4️⃣ Para Ejecutar un Ejemplo
1. Ve a la carpeta `examples/`
2. Abre el archivo del concepto que necesites
3. Copia el código SQL
4. Pégalo en Microsoft Access
5. Compara el resultado con el output esperado

---

## 🔍 Búsqueda Rápida por Categoría

### DDL - Definición de Datos
- [crear_tabla__CREATE_TABLE.sql](examples/crear_tabla__CREATE_TABLE.sql)
- [eliminar_tabla__DROP_TABLE.sql](examples/eliminar_tabla__DROP_TABLE.sql)
- [crear_indice__CREATE_INDEX.sql](examples/crear_indice__CREATE_INDEX.sql)

### DML - Inserción y Actualización
- [insertar_fila__INSERT_INTO.sql](examples/insertar_fila__INSERT_INTO.sql)
- [actualizar_con_where__UPDATE_WHERE.sql](examples/actualizar_con_where__UPDATE_WHERE.sql)
- [eliminar_con_where__DELETE_WHERE.sql](examples/eliminar_con_where__DELETE_WHERE.sql)

### Filtrado y Búsqueda
- [filtrar_where__WHERE.sql](examples/filtrar_where__WHERE.sql)
- [operador_and__AND.sql](examples/operador_and__AND.sql)
- [operador_or__OR.sql](examples/operador_or__OR.sql)
- [operador_between__BETWEEN.sql](examples/operador_between__BETWEEN.sql)
- [operador_in__IN.sql](examples/operador_in__IN.sql)
- [operador_like__LIKE.sql](examples/operador_like__LIKE.sql)

### Ordenamiento y Agrupación
- [ordenar_desc__ORDER_BY_DESC.sql](examples/ordenar_desc__ORDER_BY_DESC.sql)
- [agrupar_datos__GROUP_BY.sql](examples/agrupar_datos__GROUP_BY.sql)

### Uniones (JOINS)
- [inner_join__INNER_JOIN.sql](examples/inner_join__INNER_JOIN.sql)
- [left_join__LEFT_JOIN.sql](examples/left_join__LEFT_JOIN.sql)
- [cross_join__CROSS_JOIN.sql](examples/cross_join__CROSS_JOIN.sql)

### Funciones de Agregación
- [contar_registros__COUNT.sql](examples/contar_registros__COUNT.sql)
- [valor_minimo__MIN.sql](examples/valor_minimo__MIN.sql)
- [valor_maximo__MAX.sql](examples/valor_maximo__MAX.sql)
- [sumar_valores__SUM.sql](examples/sumar_valores__SUM.sql)
- [promedio_valores__AVG.sql](examples/promedio_valores__AVG.sql)

### Funciones de String
- [longitud_string__LEN.sql](examples/longitud_string__LEN.sql)
- [convertir_mayusculas__UCASE.sql](examples/convertir_mayusculas__UCASE.sql)
- [convertir_minusculas__LCASE.sql](examples/convertir_minusculas__LCASE.sql)

### Funciones de Fecha
- [fecha_actual__DATE.sql](examples/fecha_actual__DATE.sql)
- [diferencia_fechas__DATEDIFF.sql](examples/diferencia_fechas__DATEDIFF.sql)

### Funciones Matemáticas
- [valor_absoluto__ABS.sql](examples/valor_absoluto__ABS.sql)
- [redondear__ROUND.sql](examples/redondear__ROUND.sql)

### Control de Flujo
- [case_simple__CASE.sql](examples/case_simple__CASE.sql)
- [case_busqueda__CASE_WHEN.sql](examples/case_busqueda__CASE_WHEN.sql)

### Operaciones Conjuntas
- [union__UNION.sql](examples/union__UNION.sql)
- [union_all__UNION_ALL.sql](examples/union_all__UNION_ALL.sql)
- [eliminar_duplicados__DISTINCT.sql](examples/eliminar_duplicados__DISTINCT.sql)

### Subconsultas
- [subconsulta_where__SUBQUERY_WHERE.sql](examples/subconsulta_where__SUBQUERY_WHERE.sql)
- [subconsulta_from__SUBQUERY_FROM.sql](examples/subconsulta_from__SUBQUERY_FROM.sql)

---

## 📊 Datos de Ejemplo

### Tabla: Empleados
```
ID | Nombre              | Departamento_ID | Salario | Fecha_Contratacion
1  | Juan García         | 1              | 3500    | 2020-03-15
2  | María López         | 2              | 4200    | 2019-07-22
3  | Carlos Rodríguez    | 1              | 3800    | 2021-01-10
4  | Ana Martínez        | 3              | 4500    | 2018-11-05
5  | Pedro Sánchez       | 2              | 3900    | 2022-05-18
```

### Tabla: Departamentos
```
ID | Nombre              | Presupuesto
1  | Desarrollo          | 50000
2  | Ventas              | 35000
3  | Recursos Humanos    | 25000
```

### Tabla: Proyectos
```
ID | Nombre      | Empleado_ID | Estado      | Presupuesto
1  | Portal Web  | 1           | Activo      | 15000
2  | App Móvil   | 2           | Activo      | 25000
3  | API REST    | 3           | Completado  | 10000
4  | Dashboard   | 4           | Activo      | 12000
```

---

## 💡 Consejos de Uso

1. **Comienza por DATASET.md** para entender la estructura
2. **Lee los comentarios** en cada archivo de ejemplo
3. **Compara outputs** con lo esperado
4. **Adapta los ejemplos** a tus necesidades
5. **Agrupa aprendizaje** por categoría (DDL, DML, JOINS, etc.)

---

## ✨ Características Principales

✅ Dataset real y consistente  
✅ 30+ ejemplos actualizados  
✅ Outputs verificables  
✅ Documentación completa  
✅ Fácil navegación  
✅ Relaciones entre tablas  
✅ Casos de uso realistas  

---

## 📝 Notas Importantes

- Access utiliza `AUTOINCREMENT` para generar IDs
- Las fechas se escriben entre `#` en Access: `#2020-03-15#`
- Use `CURRENCY` para valores monetarios
- Use `TEXT(n)` para strings con longitud máxima
- Las claves foráneas (FK) vinculan las tablas

---

*Última actualización: 28 de Enero de 2026*
