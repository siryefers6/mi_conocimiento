-- Diferencia de fechas en Microsoft Access
-- Calcula los días desde la contratación hasta hoy

SELECT Nombre, Fecha_Contratacion, 
  DateDiff('d', Fecha_Contratacion, Date()) AS Dias_Trabajando
FROM Empleados;

