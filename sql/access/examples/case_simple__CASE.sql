"""
Objetivo: Clasificar datos con condiciones lógicas
Referencia: CASE
Tipo: funcion
Nivel: intermedio
"""

SELECT Nombre, Salario,
  CASE 
    WHEN Salario >= 4200 THEN 'Salario Alto'
    WHEN Salario >= 3800 THEN 'Salario Medio'
    ELSE 'Salario Bajo'
  END AS Categoria_Salario
FROM Empleados;
