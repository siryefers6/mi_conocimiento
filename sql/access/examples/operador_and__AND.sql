"""
Objetivo: Filtrar con múltiples condiciones simultáneamente
Referencia: AND
Tipo: operador
Nivel: basico
"""

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID = 1 AND Salario > 3600;
