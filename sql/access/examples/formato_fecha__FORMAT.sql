"""
Objetivo: formato fecha
Referencia: FORMAT
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT Format(fecha, 'yyyy-mm-dd') AS fecha_formateada FROM tabla;

/*output
nombre | edad | departamento
--------|------|---------------
Juan   | 30   | Ventas
Carlos | 35   | RH
*/