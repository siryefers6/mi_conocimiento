-- Insertar fila en Microsoft Access
-- Inserta un nuevo empleado en la tabla Empleados

INSERT INTO Empleados (Nombre, Departamento_ID, Salario, Fecha_Contratacion)
VALUES ('Juan García', 1, 3500, #2020-03-15#);

-- Output:
-- 1 fila insertada en Empleados
-- Registro: ID=1, Nombre='Juan García', Departamento_ID=1, Salario=3500, Fecha_Contratacion=2020-03-15