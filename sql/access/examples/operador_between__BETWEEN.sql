"""
Objetivo: Seleccionar rangos de valores
Referencia: BETWEEN
Tipo: operador
Nivel: basico
"""

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Salario BETWEEN 3700 AND 4200;
