/*
 * Objetivo: Establecer relación entre tablas con clave foránea
 * Referencia: FOREIGN KEY
 * Tipo: constraint DDL
 * Nivel: intermedio
 */

-- Crear tabla principal
CREATE TABLE IF NOT EXISTS departamentos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Crear tabla con FOREIGN KEY
CREATE TABLE IF NOT EXISTS empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento_id INT REFERENCES departamentos(id)
);

-- O definir FOREIGN KEY explícitamente
CREATE TABLE IF NOT EXISTS proyectos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- FOREIGN KEY con acciones
CREATE TABLE IF NOT EXISTS tareas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    proyecto_id INT,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Ver restricciones
\d empleados

/*
Output esperado:
Foreign-key constraints:
    "empleados_departamento_id_fkey" FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
*/
