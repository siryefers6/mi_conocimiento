/*
 * Objetivo: Crear un rol de grupo para gestionar permisos
 * Referencia: CREATE ROLE
 * Tipo: control de seguridad
 * Nivel: intermedio
 */

-- Crear rol simple (no tiene login)
-- CREATE ROLE grupo_it;

-- Crear rol con login (funciona como usuario)
-- CREATE ROLE usuario_rol WITH LOGIN PASSWORD 'pass123';

-- Crear rol con permisos predefinidos
-- CREATE ROLE admin_rol WITH CREATEDB CREATEROLE;

-- Asignar rol a un usuario
-- GRANT grupo_it TO usuario_basico;

-- Crear rol de lectura
-- CREATE ROLE lector WITH LOGIN PASSWORD 'lectura123' NOINHERIT;

-- Dar permisos al rol
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO lector;

-- Ver roles existentes
-- \du

-- Cambiar rol de usuario
-- ALTER ROLE usuario_basico SET ROLE grupo_it;

-- Eliminar rol
-- DROP ROLE grupo_it;

/*
Diferencia entre ROLE y USER:
- ROLE: Grupo para gestionar permisos
- USER: ROLE con capacidad de login

Un usuario puede ser miembro de múltiples roles.
*/
