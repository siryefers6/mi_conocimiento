/*
 * Objetivo: Sumar valores de una columna
 * Referencia: SUM()
 * Tipo: función de agregación
 * Nivel: básico
 */

-- Crear tabla de ejemplo
CREATE TABLE IF NOT EXISTS facturas (
    id SERIAL PRIMARY KEY,
    numero INT,
    cliente VARCHAR(100),
    monto DECIMAL(10,2)
);

-- Insertar datos de prueba
INSERT INTO facturas (numero, cliente, monto)
VALUES
    (1001, 'Empresa A', 5000),
    (1002, 'Empresa B', 3500),
    (1003, 'Empresa A', 2000),
    (1004, 'Empresa C', 7500),
    (1005, 'Empresa B', 4200);

-- SUM básico
SELECT SUM(monto) as total_ventas FROM facturas;

-- SUM con WHERE
SELECT SUM(monto) as total_empresaA FROM facturas WHERE cliente = 'Empresa A';

-- SUM con GROUP BY
SELECT cliente, SUM(monto) as total_por_cliente
FROM facturas
GROUP BY cliente
ORDER BY total_por_cliente DESC;

-- SUM con condición en GROUP BY
SELECT cliente, COUNT(*) as facturas, SUM(monto) as total
FROM facturas
GROUP BY cliente
HAVING SUM(monto) > 5000;

/*
Output esperado:
 total_ventas
--------------
 22200.00
*/
