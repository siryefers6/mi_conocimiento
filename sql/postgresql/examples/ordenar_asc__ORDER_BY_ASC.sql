/*
 * Objetivo: Ordenar resultados en forma ascendente
 * Referencia: ORDER BY ASC
 * Tipo: DQL (Data Query Language)
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150),
    autor VARCHAR(100),
    anio INT,
    precio DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO libros (titulo, autor, anio, precio)
VALUES
    ('El Quijote', 'Cervantes', 1605, 25.99),
    ('1984', 'George Orwell', 1949, 15.99),
    ('Cien años de soledad', 'García Márquez', 1967, 22.99),
    ('Orgullo y prejuicio', 'Jane Austen', 1813, 18.99),
    ('El Gran Gatsby', 'F. Scott Fitzgerald', 1925, 19.99);

-- ORDER BY ASC (ascendente)
SELECT titulo, anio FROM libros ORDER BY anio ASC;

-- ORDER BY ascendente sin especificar ASC (es el default)
SELECT titulo, precio FROM libros ORDER BY precio;

-- ORDER BY múltiples columnas
SELECT * FROM libros ORDER BY autor ASC, anio ASC;

/*
Output esperado:
      titulo      | anio
------------------|------
 Orgullo y prejuicio | 1813
 El Quijote | 1605
 El Gran Gatsby | 1925
 1984 | 1949
 Cien años de soledad | 1967
*/
