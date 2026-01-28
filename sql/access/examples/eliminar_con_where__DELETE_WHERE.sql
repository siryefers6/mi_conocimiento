-- Eliminar con WHERE en Microsoft Access
-- Elimina proyectos completados de la tabla Proyectos

DELETE FROM Proyectos WHERE Estado = 'Completado';

-- Output:
-- 1 registro eliminado (API REST con ID=3)