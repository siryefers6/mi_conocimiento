/*
 * Objetivo: Crear función con parámetros de entrada
 * Referencia: FUNCTION(params)
 * Tipo: PL/pgSQL
 * Nivel: intermedio
 */

-- Función con parámetros IN
CREATE OR REPLACE FUNCTION calcular_descuento(
    p_precio DECIMAL,
    p_porcentaje DECIMAL
)
RETURNS DECIMAL AS $$
DECLARE
    v_descuento DECIMAL;
BEGIN
    v_descuento := p_precio * (p_porcentaje / 100);
    RETURN v_descuento;
END;
$$ LANGUAGE plpgsql;

-- Usar función parametrizada
SELECT calcular_descuento(100, 20) as descuento;

-- Función con múltiples parámetros
CREATE OR REPLACE FUNCTION clasificar_estado(
    p_edad INT,
    p_salario DECIMAL
)
RETURNS VARCHAR AS $$
BEGIN
    IF p_edad < 18 THEN
        RETURN 'Menor de edad';
    ELSIF p_salario > 5000 THEN
        RETURN 'Alto sueldo';
    ELSE
        RETURN 'Regular';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Usar función
SELECT 
    clasificar_estado(25, 6000) as estado1,
    clasificar_estado(16, 3000) as estado2;

/*
Output esperado:
 descuento
-----------
 20.00
*/
