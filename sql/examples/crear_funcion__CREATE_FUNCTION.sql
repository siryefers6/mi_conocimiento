/*
 * Objetivo: Crear una función reutilizable
 * Referencia: CREATE FUNCTION
 * Tipo: PL/pgSQL
 * Nivel: intermedio
 */

-- Crear función simple
CREATE OR REPLACE FUNCTION calcular_edad(fecha_naci DATE)
RETURNS INT AS $$
BEGIN
    RETURN EXTRACT(YEAR FROM AGE(fecha_naci));
END;
$$ LANGUAGE plpgsql;

-- Usar la función
SELECT calcular_edad('1990-05-15') as edad;

-- Crear función con múltiples parámetros
CREATE OR REPLACE FUNCTION sumar(a INT, b INT)
RETURNS INT AS $$
BEGIN
    RETURN a + b;
END;
$$ LANGUAGE plpgsql;

-- Usar la función
SELECT sumar(10, 20) as resultado;

-- Crear tabla y usar función
CREATE TABLE IF NOT EXISTS personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_naci DATE
);

INSERT INTO personas (nombre, fecha_naci)
VALUES ('Juan', '1990-05-15'), ('María', '1985-03-20');

SELECT nombre, calcular_edad(fecha_naci) as edad FROM personas;

/*
Output esperado:
 edad
------
 34
*/
