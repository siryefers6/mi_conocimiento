-- Restricción CHECK en Microsoft Access
-- Nota: Access no soporta CHECK constraints en SQL; usar validación en formulario.
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    edad INTEGER
);