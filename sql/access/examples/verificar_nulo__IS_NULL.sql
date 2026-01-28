"""
Objetivo: verificar nulo
Referencia: IS_NULL
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT * FROM empleados WHERE departamento IS NULL;

/*output
id | nombre | telefono
----|--------|----------
5  | Pedro  | NULL
*/