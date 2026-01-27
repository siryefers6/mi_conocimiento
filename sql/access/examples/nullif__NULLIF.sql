-- NULLIF en Microsoft Access
-- Nota: Access no tiene NULLIF; usar IIf().
SELECT IIf(campo = 'valor', Null, campo) FROM tabla;