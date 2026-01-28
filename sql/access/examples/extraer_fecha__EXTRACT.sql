"""
Objetivo: extraer partes de una fecha (año, mes, día)
Referencia: YEAR, MONTH, DAY
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT 
    YEAR(fecha_nac) AS anio,
    MONTH(fecha_nac) AS mes,
    DAY(fecha_nac) AS dia
FROM empleados;

/*output
anio | mes | dia
------|-----|----
1990 | 5   | 15
1985 | 12  | 3
1992 | 8   | 22
*/