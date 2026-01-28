-- CASE búsqueda en Microsoft Access
-- Clasifica proyectos según su estado

SELECT Nombre, Presupuesto, Estado,
  CASE Estado
    WHEN 'Activo' THEN 'En ejecución'
    WHEN 'Completado' THEN 'Finalizado'
    WHEN 'Pausado' THEN 'Temporalmente detenido'
    ELSE 'Desconocido'
  END AS Clasificacion
FROM Proyectos;

