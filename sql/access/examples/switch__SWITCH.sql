"""
Objetivo: switch
Referencia: SWITCH
Tipo: funcion
Nivel: basico
"""

-- transformacion
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

