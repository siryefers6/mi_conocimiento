"""
Objetivo: Buscar patrones de texto
Referencia: LIKE
Tipo: operador
Nivel: basico
"""

SELECT ID, Nombre, Departamento_ID, Salario 
FROM Empleados 
WHERE Nombre LIKE 'M*';
