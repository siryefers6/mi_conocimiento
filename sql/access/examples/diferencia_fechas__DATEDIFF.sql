-- Diferencia de fechas en Microsoft Access
-- Calcula los días desde la contratación hasta hoy

SELECT Nombre, Fecha_Contratacion, 
  DateDiff('d', Fecha_Contratacion, Date()) AS Dias_Trabajando
FROM Empleados;

-- Output:
-- Nombre           | Fecha_Contratacion | Dias_Trabajando
-- -------------- | --------------- | ----------------
-- Juan García     | 2020-03-15          | 2185
-- María López     | 2019-07-22          | 2386
-- Carlos Rodríguez | 2021-01-10          | 1843
-- Ana Martínez    | 2018-11-05          | 2545
-- Pedro Sánchez   | 2022-05-18          | 1420