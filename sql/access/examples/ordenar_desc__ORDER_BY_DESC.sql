"""
Objetivo: Ordenar resultados en forma descendente
Referencia: ORDER_BY_DESC
Tipo: select
Nivel: basico
"""

SELECT ID, Nombre, Departamento_ID, Salario, Fecha_Contratacion
FROM Empleados
ORDER BY Salario DESC;
