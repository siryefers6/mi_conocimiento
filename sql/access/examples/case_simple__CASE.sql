-- CASE simple en Microsoft Access
-- Clasifica empleados según su salario

SELECT Nombre, Salario,
  CASE 
    WHEN Salario >= 4200 THEN 'Salario Alto'
    WHEN Salario >= 3800 THEN 'Salario Medio'
    ELSE 'Salario Bajo'
  END AS Categoria_Salario
FROM Empleados;

-- Output:
-- Nombre           | Salario | Categoria_Salario
-- -------------- | ------- | -----------------
-- Juan García     | 3500    | Salario Bajo
-- María López     | 4200    | Salario Alto
-- Carlos Rodríguez | 3800    | Salario Medio
-- Ana Martínez    | 4500    | Salario Alto
-- Pedro Sánchez   | 3900    | Salario Medio