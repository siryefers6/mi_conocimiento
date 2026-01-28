-- Crear tabla en Microsoft Access
-- Nota: Access usa tipos como INTEGER, TEXT, CURRENCY, DATE, etc.
-- Este ejemplo crea la tabla Empleados del dataset

CREATE TABLE Empleados (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT(100) NOT NULL,
    Departamento_ID INTEGER,
    Salario CURRENCY,
    Fecha_Contratacion DATE,
    FOREIGN KEY (Departamento_ID) REFERENCES Departamentos(ID)
);

