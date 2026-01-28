"""
Objetivo: Usar consultas anidadas para filtrado avanzado
Referencia: SUBQUERY_WHERE
Tipo: select
Nivel: avanzado
"""

SELECT ID, Nombre, Salario
FROM Empleados
WHERE Salario > (SELECT AVG(Salario) FROM Empleados);
