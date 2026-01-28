# FAQ - Preguntas Frecuentes

## General

### ¿Cuál es la mejor forma de empezar?
1. Abre [DATASET.md](DATASET.md) y entende la estructura
2. Lee [GUIA_MEJORAS.md](GUIA_MEJORAS.md) para ver qué cambió
3. Abre [INDEX.md](INDEX.md) para navegar por los ejemplos
4. Elige un concepto que te interese y abre el ejemplo

### ¿Dónde encuentro un concepto específico?
Usa [INDEX.md](INDEX.md) que tiene búsqueda rápida por categoría, o consulta [README.md](README.md) para la lista completa.

### ¿Qué es el "dataset"?
Es un conjunto de 3 tablas SQL (Empleados, Departamentos, Proyectos) con datos realistas que se usan en todos los ejemplos para ser consistentes y verificables.

---

## Dataset

### ¿Cuántas tablas tiene el dataset?
3 tablas:
- **Empleados**: 5 registros
- **Departamentos**: 3 registros  
- **Proyectos**: 4 registros

### ¿Puedo modificar el dataset?
Sí, los ejemplos son una guía. Adapta el dataset a tus necesidades educativas.

### ¿Dónde veo la estructura exacta?
En [DATASET.md](DATASET.md) encontrarás:
- Estructura de cada tabla
- Datos de ejemplo
- Scripts SQL para crear las tablas

### ¿El dataset tiene relaciones entre tablas?
Sí:
- **Empleados → Departamentos**: A través de `Departamento_ID`
- **Empleados → Proyectos**: A través de `Empleado_ID`

---

## Ejemplos

### ¿Cuántos ejemplos hay?
110 ejemplos distribuidos en todas las categorías de SQL.

### ¿Cuántos fueron actualizados?
27 ejemplos fueron completamente reescritos con datos reales y outputs verificables.

### ¿Cómo uso un ejemplo?
1. Abre el archivo `.sql` 
2. Copia el código SQL
3. Pégalo en Microsoft Access
4. Compara tu resultado con el "Output" mostrado en comentarios

### ¿Por qué incluyen "Output" los ejemplos?
Para que verifiques que tu resultado es correcto. Si tu output coincide con el esperado, ¡lo hiciste bien!

### ¿Debo memorizar los ejemplos?
No. Usa los ejemplos como referencia. Lo importante es entender **cómo funciona** cada concepto.

---

## SQL en Access

### ¿Cuál es la sintaxis de fechas en Access?
Usa `#` alrededor de las fechas: `#2020-03-15#`

Ejemplo:
```sql
WHERE Fecha_Contratacion = #2020-03-15#
```

### ¿Cómo genero IDs automáticos?
Usa `AUTOINCREMENT` en la clave primaria:
```sql
ID INTEGER PRIMARY KEY AUTOINCREMENT
```

### ¿Qué tipo de dato uso para dinero?
Usa `CURRENCY`:
```sql
Salario CURRENCY
```

### ¿Cómo creo una relación entre tablas?
Usa `FOREIGN KEY`:
```sql
FOREIGN KEY (Departamento_ID) REFERENCES Departamentos(ID)
```

### ¿Cuál es la diferencia entre INNER JOIN y LEFT JOIN?
- **INNER JOIN**: Solo coincidencias
- **LEFT JOIN**: Todas las filas de la izquierda + coincidencias

---

## Mejoras y Cambios

### ¿Qué mejoró exactamente?
Consulta [CAMBIOS_REALIZADOS.txt](CAMBIOS_REALIZADOS.txt) para lista completa:
- Dataset consistente
- 27 ejemplos reescritos
- Outputs verificables
- Documentación nueva

### ¿Por qué estos cambios?
Porque muchos ejemplos tenían:
- Nombres de tabla inconsistentes
- Datos ficticios sin sentido
- Outputs incorrectos o faltantes
- Referencias a tablas inexistentes

### ¿Los ejemplos antiguos siguen siendo válidos?
Parcialmente. Muchos se pueden adaptar, pero los actualizados son más confiables.

---

## Documentación

### ¿Cuál es la diferencia entre estos archivos?

| Archivo | Para qué |
|---------|----------|
| **INDEX.md** | Navegación rápida (COMIENZA AQUÍ) |
| **DATASET.md** | Entender la estructura de datos |
| **GUIA_MEJORAS.md** | Qué cambió y cómo usar |
| **CAMBIOS_REALIZADOS.txt** | Resumen ejecutivo detallado |
| **README.md** | Referencia completa de SQL |

### ¿Debo leerlo todo?
No obligatoriamente. Comienza con [INDEX.md](INDEX.md) y luego abre los ejemplos que necesites.

---

## Ejecución

### ¿Cómo ejecuto un ejemplo en Access?
1. Abre Microsoft Access
2. Crea una nueva base de datos
3. Ejecuta los scripts de [DATASET.md](DATASET.md) para crear tablas
4. Inserta los datos de ejemplo
5. Copia y pega el código SQL del ejemplo
6. Presiona Enter o ejecuta la consulta

### ¿Qué si no tengo Access?
Puedes usar:
- **SQLite** (necesita sintaxis adaptada)
- **MySQL** (necesita sintaxis adaptada)
- **PostgreSQL** (necesita sintaxis adaptada)
- **SQL Server** (muy similar a Access)

### ¿Cómo adapto un ejemplo a otra base de datos?
Los cambios principales serían:
- Sintaxis de fechas
- Tipos de dato
- Nombres de funciones
- Claves foráneas

---

## Contribución

### ¿Encontré un error, qué hago?
Documenta:
- Qué archivo tiene el error
- Cuál es el problema
- Cuál debería ser el resultado correcto

### ¿Puedo agregar más ejemplos?
Sí, sigue este formato:
```sql
-- CONCEPTO en Microsoft Access
-- Descripción de qué hace

[CÓDIGO SQL AQUÍ]

-- Output:
-- [RESULTADO ESPERADO AQUÍ]
```

---

## Recursos Relacionados

### ¿Dónde aprender SQL?
- [Microsoft Access SQL Docs](https://support.microsoft.com/en-us/office/basic-data-types-in-access-23d1b67e-ac33-4352-ab78-7efb69eeb59a)
- W3Schools SQL Tutorial
- Khan Academy SQL

### ¿Hay libros recomendados?
- "Learning SQL" - Alan Beaulieu
- "SQL Performance Explained" - Markus Winand
- "SQL Queries for Mere Mortals" - Michael J. Hernandez

---

## Solución de Problemas

### Mi consulta no funciona, ¿qué hago?
1. Verifica los nombres de tabla y columnas
2. Revisa la sintaxis SQL
3. Compara con el ejemplo correspondiente
4. Verifica que existan registros para consultar
5. Lee los comentarios SQL en el ejemplo

### ¿Por qué me dice "tabla no encontrada"?
- No creaste la tabla
- El nombre está mal escrito
- Escríbelo exactamente como aparece en DATASET.md

### ¿Por qué el output no coincide?
- Tienes datos diferentes
- Tu SQL es ligeramente diferente
- Hay registros duplicados o faltantes

---

*Última actualización: 28 de Enero de 2026*
