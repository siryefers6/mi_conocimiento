-- Clave foránea en Microsoft Access
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT(50),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departamentos(id)
);