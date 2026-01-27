-- IIF() - Función Condicional Simple
-- Evalúa una condición y devuelve uno de dos valores basado en el resultado
-- Sintaxis: IIF(condición, valor_si_verdadero, valor_si_falso)

-- Ejemplo 1: IIF simple
SELECT 
    ProductoID,
    Nombre,
    Precio,
    IIF(Precio > 100, 'Caro', 'Barato') AS Categoría
FROM Productos;

-- Ejemplo 2: IIF con comparación
SELECT 
    EmpleadoID,
    Nombre,
    Salario,
    IIF(Salario >= 50000, 'Senior', 'Junior') AS Nivel
FROM Empleados;

-- Ejemplo 3: IIF anidado (múltiples condiciones)
SELECT 
    ClienteID,
    Nombre,
    Monto,
    IIF(Monto >= 1000, 'Premium', IIF(Monto >= 500, 'Gold', 'Regular')) AS TipoCliente
FROM Clientes;

-- Ejemplo 4: IIF con NULL
SELECT 
    PersonaID,
    Nombre,
    Teléfono,
    IIF(Teléfono IS NULL, 'Sin contacto', Teléfono) AS ContactoActual
FROM Personas;

-- Ejemplo 5: IIF en cálculos
SELECT 
    VentaID,
    Cantidad,
    Precio,
    IIF(Cantidad > 10, Cantidad * Precio * 0.9, Cantidad * Precio) AS MontoFinal
FROM Ventas;
