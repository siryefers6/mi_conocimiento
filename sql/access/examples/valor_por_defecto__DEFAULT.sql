-- Valor por defecto en Microsoft Access
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT(50),
    activo YESNO DEFAULT YES
);