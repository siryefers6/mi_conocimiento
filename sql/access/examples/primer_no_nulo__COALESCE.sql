-- COALESCE en Microsoft Access
-- Nota: Access no tiene COALESCE; usar Nz().
SELECT Nz(campo, 'default') FROM tabla;