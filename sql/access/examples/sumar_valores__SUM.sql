-- SUM en Microsoft Access
-- Calcula el total de presupuesto asignado a todos los proyectos

SELECT SUM(Presupuesto) AS Presupuesto_Total FROM Proyectos;

-- Output:
-- Presupuesto_Total
-- -----------------
-- 62000