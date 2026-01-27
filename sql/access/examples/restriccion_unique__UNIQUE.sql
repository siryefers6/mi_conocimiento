-- Restricción UNIQUE en Microsoft Access
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    email TEXT(50) UNIQUE
);