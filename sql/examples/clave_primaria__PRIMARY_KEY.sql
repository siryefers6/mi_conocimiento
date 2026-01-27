/*
 * Objetivo: Definir clave primaria para identificar filas únicamente
 * Referencia: PRIMARY KEY
 * Tipo: constraint DDL
 * Nivel: básico
 */

-- Crear tabla con PRIMARY KEY en definición
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

-- O definir PRIMARY KEY de otra forma
CREATE TABLE IF NOT EXISTS productos (
    id INT,
    nombre VARCHAR(100),
    PRIMARY KEY (id)
);

-- PRIMARY KEY compuesta (múltiples columnas)
CREATE TABLE IF NOT EXISTS pedidos (
    usuario_id INT,
    producto_id INT,
    cantidad INT,
    PRIMARY KEY (usuario_id, producto_id)
);

-- Ver restricciones
\d usuarios

/*
Output esperado:
Indexes:
    "usuarios_pkey" PRIMARY KEY, btree (id)
*/
