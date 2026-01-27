/*
 * Objetivo: Crear un nuevo usuario en PostgreSQL
 * Referencia: CREATE USER
 * Tipo: control de seguridad
 * Nivel: intermedio
 */

-- Crear usuario simple
-- CREATE USER usuario_basico;

-- Crear usuario con contraseña
-- CREATE USER usuario_seguro WITH PASSWORD 'contraseña_fuerte';

-- Crear usuario con opciones
-- CREATE USER usuario_activo 
--   WITH PASSWORD 'pass123'
--   VALID UNTIL '2025-12-31'
--   IN ROLE grupo_usuarios;

-- Crear usuario superuser
-- CREATE USER administrador WITH SUPERUSER PASSWORD 'admin123';

-- Crear usuario solo lectura
-- CREATE USER reportero WITH PASSWORD 'read123';
-- GRANT CONNECT ON DATABASE mi_bd TO reportero;

-- Ver usuarios existentes
-- \du

-- Cambiar contraseña de usuario
-- ALTER USER usuario_basico WITH PASSWORD 'nueva_contraseña';

-- Eliminar usuario
-- DROP USER usuario_basico;

/*
Opciones CREATE USER:
- WITH PASSWORD: Contraseña
- SUPERUSER/NOSUPERUSER: Privilegios de admin
- CREATEDB/NOCREATEDB: Crear bases de datos
- CREATEROLE/NOCREATEROLE: Crear roles
- VALID UNTIL: Fecha de expiración
*/
