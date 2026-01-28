"""
Objetivo: iif
Referencia: IIF
Tipo: funcion
Nivel: basico
"""

-- transformacion
SELECT 
    ProductoID,
    Nombre,
    Precio,
    IIF(Precio > 100, 'Caro', 'Barato') AS Categoría
FROM Productos;
SELECT 
    EmpleadoID,
    Nombre,
    Salario,
    IIF(Salario >= 50000, 'Senior', 'Junior') AS Nivel
FROM Empleados;
SELECT 
    ClienteID,
    Nombre,
    Monto,
    IIF(Monto >= 1000, 'Premium', IIF(Monto >= 500, 'Gold', 'Regular')) AS TipoCliente
FROM Clientes;
SELECT 
    PersonaID,
    Nombre,
    Teléfono,
    IIF(Teléfono IS NULL, 'Sin contacto', Teléfono) AS ContactoActual
FROM Personas;
SELECT 
    VentaID,
    Cantidad,
    Precio,
    IIF(Cantidad > 10, Cantidad * Precio * 0.9, Cantidad * Precio) AS MontoFinal
FROM Ventas;

/*output
nombre | edad | categoria
--------|------|----------
Juan   | 30   | Mayor
María  | 28   | Menor
Carlos | 35   | Mayor
*/