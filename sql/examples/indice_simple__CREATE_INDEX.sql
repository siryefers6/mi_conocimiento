/*
 * Objetivo: Crear un índice simple para optimizar búsquedas
 * Referencia: CREATE INDEX
 * Tipo: optimización
 * Nivel: intermedio
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    autor VARCHAR(100),
    isbn VARCHAR(20)
);

-- Insertar datos
INSERT INTO libros (titulo, autor, isbn)
VALUES
    ('1984', 'George Orwell', '978-0451524935'),
    ('El Quijote', 'Cervantes', '978-8424139049'),
    ('Cien años de soledad', 'García Márquez', '978-8401495561');

-- Crear índice simple
CREATE INDEX idx_libros_autor ON libros(autor);

-- Crear índice en múltiples columnas
CREATE INDEX idx_libros_titulo_autor ON libros(titulo, autor);

-- Ver índices
\di libros

-- Consulta que usa el índice
SELECT * FROM libros WHERE autor = 'George Orwell';

/*
Los índices aceleran búsquedas pero ralentizan inserciones/actualizaciones.
Usar en columnas frecuentemente consultadas (WHERE, JOIN).
*/
