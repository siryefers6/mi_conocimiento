-- CASE simple en Microsoft Access
-- Clasifica empleados según su salario

SELECT Nombre, Salario,
  CASE 
    WHEN Salario >= 4200 THEN 'Salario Alto'
    WHEN Salario >= 3800 THEN 'Salario Medio'
    ELSE 'Salario Bajo'
  END AS Categoria_Salario
FROM Empleados;

