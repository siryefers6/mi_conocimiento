"""
Objetivo: Filtrar con al menos una condición cumplida
Referencia: OR
Tipo: operador
Nivel: basico
"""

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID = 1 OR Departamento_ID = 3;
