-- Renombrar columna en Microsoft Access
-- Nota: Access no soporta RENAME COLUMN directamente; usar ALTER TABLE con ADD y DROP.
ALTER TABLE empleados ADD COLUMN nombre_completo TEXT(50);
ALTER TABLE empleados DROP COLUMN nombre;