/*
 * Objetivo: Revocar (quitar) permisos a usuarios
 * Referencia: REVOKE
 * Tipo: control de seguridad
 * Nivel: intermedio
 */

-- Crear usuario de prueba
-- CREATE USER usuario_temporal WITH PASSWORD 'temporal123';

-- Otorgar permisos
-- GRANT SELECT ON usuarios TO usuario_temporal;

-- Revocar permisos específicos
-- REVOKE SELECT ON usuarios FROM usuario_temporal;

-- Revocar todos los permisos
-- REVOKE ALL ON usuarios FROM usuario_temporal;

-- Revocar permisos en múltiples tablas
-- REVOKE SELECT, INSERT ON usuarios, productos FROM usuario_temporal;

-- Revocar permisos de esquema
-- REVOKE USAGE ON SCHEMA public FROM usuario_temporal;

-- Revocar y redistribuir a CASCADE
-- REVOKE ALL ON ALL TABLES IN SCHEMA public FROM usuario_temporal CASCADE;

-- Ver permisos finales
-- \dp usuarios

/*
REVOKE es lo opuesto a GRANT.
- Elimina permisos específicos
- Puede ser selectivo (solo SELECT)
- CASCADE propaga la revocación

Importante: Un usuario sin permisos no puede acceder a las tablas.
*/
