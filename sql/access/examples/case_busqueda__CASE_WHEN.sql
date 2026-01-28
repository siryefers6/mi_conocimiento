"""
Objetivo: Asignar valores basado en múltiples condiciones
Referencia: CASE_WHEN
Tipo: funcion
Nivel: intermedio
"""

SELECT Nombre, Presupuesto, Estado,
  CASE Estado
    WHEN 'Activo' THEN 'En ejecución'
    WHEN 'Completado' THEN 'Finalizado'
    WHEN 'Pausado' THEN 'Temporalmente detenido'
    ELSE 'Desconocido'
  END AS Clasificacion
FROM Proyectos;
