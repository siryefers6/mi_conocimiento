/*
 * Objetivo: Validar que valores cumplan una condición específica
 * Referencia: CHECK
 * Tipo: constraint DDL
 * Nivel: intermedio
 */

-- CHECK en una columna
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT CHECK (edad >= 18),
    salario DECIMAL(10,2) CHECK (salario > 0)
);

-- CHECK con múltiples condiciones
CREATE TABLE IF NOT EXISTS cursos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    duracion_horas INT CHECK (duracion_horas > 0),
    estudiantes INT CHECK (estudiantes >= 0 AND estudiantes <= 50)
);

-- CHECK con nombre explícito
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    CONSTRAINT pk_precio_positivo CHECK (precio > 0)
);

-- Ver restricciones
\d empleados

/*
Output esperado:
Check constraints:
    "empleados_edad_check" CHECK ((edad >= 18))
    "empleados_salario_check" CHECK ((salario > 0))
*/
