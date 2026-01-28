"""
Objetivo: Calcular la diferencia entre dos fechas
Referencia: DATEDIFF
Tipo: funcion
Nivel: intermedio
"""

SELECT Nombre, Fecha_Contratacion, 
  DateDiff('d', Fecha_Contratacion, Date()) AS Dias_Trabajando
FROM Empleados;
