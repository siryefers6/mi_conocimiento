/*
 * Objetivo: Otorgar permisos a usuarios
 * Referencia: GRANT
 * Tipo: control de seguridad
 * Nivel: intermedio
 */

-- Crear usuario (requiere superuser)
-- CREATE USER usuario_lectura WITH PASSWORD 'contraseña';

-- Otorgar permisos de SELECT en tabla
-- GRANT SELECT ON usuarios TO usuario_lectura;

-- Otorgar múltiples permisos
-- GRANT SELECT, INSERT ON usuarios TO usuario_lectura;

-- Otorgar permisos en todas las tablas
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO usuario_lectura;

-- Otorgar permisos en secuencias (para SERIAL)
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO usuario_lectura;

-- Otorgar permisos en esquema
-- GRANT USAGE ON SCHEMA public TO usuario_lectura;

-- Ver permisos
-- \dp usuarios

/*
Permisos comunes:
- SELECT: Leer datos
- INSERT: Insertar datos
- UPDATE: Modificar datos
- DELETE: Eliminar datos
- EXECUTE: Ejecutar funciones
- USAGE: Usar secuencias o esquemas

Ejemplo:
GRANT SELECT, INSERT, UPDATE ON usuarios TO usuario_app;
*/
