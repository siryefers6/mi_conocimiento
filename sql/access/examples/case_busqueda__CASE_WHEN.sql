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

-- Output:
-- Nombre      | Presupuesto | Estado      | Clasificacion
-- ---------- | ---------- | ----------- | ------------------
-- Portal Web  | 15000      | Activo      | En ejecución
-- App Móvil   | 25000      | Activo      | En ejecución
-- API REST    | 10000      | Completado  | Finalizado
-- Dashboard   | 12000      | Activo      | En ejecución