"""
Objetivo: Definir la estructura de una nueva tabla
Referencia: CREATE_TABLE
Tipo: ddl
Nivel: basico
"""

CREATE TABLE Empleados (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT(100) NOT NULL,
    Departamento_ID INTEGER,
    Salario CURRENCY,
    Fecha_Contratacion DATE,
    FOREIGN KEY (Departamento_ID) REFERENCES Departamentos(ID)
);
