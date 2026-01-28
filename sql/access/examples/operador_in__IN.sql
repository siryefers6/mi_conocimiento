"""
Objetivo: Filtrar por múltiples valores específicos
Referencia: IN
Tipo: operador
Nivel: basico
"""

SELECT ID, Nombre, Departamento_ID, Salario
FROM Empleados
WHERE Departamento_ID IN (1, 2);
