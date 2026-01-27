/*
 * Objetivo: Garantizar que valores en columna sean únicos
 * Referencia: UNIQUE
 * Tipo: constraint DDL
 * Nivel: básico
 */

-- Definir UNIQUE en columna individual
CREATE TABLE IF NOT EXISTS cuentas (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- UNIQUE en múltiples columnas
CREATE TABLE IF NOT EXISTS registros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    UNIQUE (nombre, apellido)
);

-- Agregar restricción UNIQUE a tabla existente
ALTER TABLE usuarios ADD CONSTRAINT uk_email UNIQUE (email);

-- Ver restricciones
\d cuentas

/*
Output esperado:
Indexes:
    "cuentas_pkey" PRIMARY KEY, btree (id)
    "cuentas_username_key" UNIQUE CONSTRAINT, btree (username)
    "cuentas_email_key" UNIQUE CONSTRAINT, btree (email)
*/
