-- SWITCH() - Función Condicional Múltiple
-- Evalúa múltiples condiciones y devuelve el valor correspondiente
-- Sintaxis: SWITCH(expr1, valor1, expr2, valor2, ..., [valor_predeterminado])

-- Ejemplo 1: SWITCH simple
SELECT 
    EstadoID,
    Nombre,
    SWITCH(
        EstadoID, 1, 'Activo',
        EstadoID, 2, 'Inactivo',
        EstadoID, 3, 'Suspendido',
        'Desconocido'
    ) AS EstadoDescripción
FROM Usuarios;

-- Ejemplo 2: SWITCH con estados numéricos
SELECT 
    PedidoID,
    FechaPedido,
    SWITCH(
        Estado, 1, 'Pendiente',
        Estado, 2, 'En proceso',
        Estado, 3, 'Enviado',
        Estado, 4, 'Entregado',
        Estado, 5, 'Cancelado',
        'Error'
    ) AS EstadoPedido
FROM Pedidos;

-- Ejemplo 3: SWITCH con clasificación de edad
SELECT 
    PersonaID,
    Nombre,
    Edad,
    SWITCH(
        Edad < 18, 'Menor',
        Edad < 30, 'Joven',
        Edad < 60, 'Adulto',
        'Jubilado'
    ) AS Categoría
FROM Personas;

-- Ejemplo 4: SWITCH con calificaciones
SELECT 
    EstudianteID,
    Nombre,
    Calificación,
    SWITCH(
        Calificación >= 90, 'A',
        Calificación >= 80, 'B',
        Calificación >= 70, 'C',
        Calificación >= 60, 'D',
        'F'
    ) AS Grado
FROM Estudiantes;

-- Ejemplo 5: SWITCH con categorías de productos
SELECT 
    ProductoID,
    Nombre,
    Categoría,
    SWITCH(
        Categoría, 'A', 'Electrónica',
        Categoría, 'B', 'Ropa',
        Categoría, 'C', 'Libros',
        Categoría, 'D', 'Alimentos',
        'Otros'
    ) AS DescripciónCategoría
FROM Productos;
