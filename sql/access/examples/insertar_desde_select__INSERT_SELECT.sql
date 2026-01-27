-- Insertar desde SELECT en Microsoft Access
INSERT INTO empleados_backup (id, nombre, edad)
SELECT id, nombre, edad FROM empleados;