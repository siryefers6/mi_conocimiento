# Dataset de Ejemplo - Microsoft Access SQL

Este documento describe el dataset utilizado en los ejemplos de SQL Access.

## Estructura de las Tablas

### Tabla: Empleados
```
ID (INTEGER, PRIMARY KEY) | Nombre (TEXT) | Departamento_ID (INTEGER, FK) | Salario (CURRENCY) | Fecha_Contratacion (DATE)
```

| ID | Nombre | Departamento_ID | Salario | Fecha_Contratacion |
|----|--------|-----------------|---------|-------------------|
| 1 | Juan García | 1 | 3500 | 2020-03-15 |
| 2 | María López | 2 | 4200 | 2019-07-22 |
| 3 | Carlos Rodríguez | 1 | 3800 | 2021-01-10 |
| 4 | Ana Martínez | 3 | 4500 | 2018-11-05 |
| 5 | Pedro Sánchez | 2 | 3900 | 2022-05-18 |

### Tabla: Departamentos
```
ID (INTEGER, PRIMARY KEY) | Nombre (TEXT) | Presupuesto (CURRENCY)
```

| ID | Nombre | Presupuesto |
|----|--------|-------------|
| 1 | Desarrollo | 50000 |
| 2 | Ventas | 35000 |
| 3 | Recursos Humanos | 25000 |

### Tabla: Proyectos
```
ID (INTEGER, PRIMARY KEY) | Nombre (TEXT) | Empleado_ID (INTEGER, FK) | Estado (TEXT) | Presupuesto (CURRENCY)
```

| ID | Nombre | Empleado_ID | Estado | Presupuesto |
|----|--------|-------------|--------|------------|
| 1 | Portal Web | 1 | Activo | 15000 |
| 2 | App Móvil | 2 | Activo | 25000 |
| 3 | API REST | 3 | Completado | 10000 |
| 4 | Dashboard | 4 | Activo | 12000 |

## Scripts de Creación

### Crear tabla Empleados
```sql
CREATE TABLE Empleados (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT(100) NOT NULL,
    Departamento_ID INTEGER,
    Salario CURRENCY,
    Fecha_Contratacion DATE,
    FOREIGN KEY (Departamento_ID) REFERENCES Departamentos(ID)
);
```

### Crear tabla Departamentos
```sql
CREATE TABLE Departamentos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT(100) NOT NULL,
    Presupuesto CURRENCY
);
```

### Crear tabla Proyectos
```sql
CREATE TABLE Proyectos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT(100) NOT NULL,
    Empleado_ID INTEGER,
    Estado TEXT(50),
    Presupuesto CURRENCY,
    FOREIGN KEY (Empleado_ID) REFERENCES Empleados(ID)
);
```

## Notas Importantes

- Access utiliza `AUTOINCREMENT` para generar IDs automáticamente
- Los tipos CURRENCY se usan para valores monetarios
- Las claves foráneas (FK) vinculan las tablas
- El dataset está diseñado para ejemplificar relaciones 1:N entre tablas
