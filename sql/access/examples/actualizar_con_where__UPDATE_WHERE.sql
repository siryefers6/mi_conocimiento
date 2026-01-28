"""
Objetivo: Modificar registros con condiciones específicas
Referencia: UPDATE WHERE
Tipo: dml
Nivel: basico
"""

UPDATE Empleados 
SET Salario = Salario * 1.05 
WHERE Departamento_ID = 1;
