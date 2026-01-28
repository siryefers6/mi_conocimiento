# Roadmap de Aprendizaje Python

## Estructura de Contenido

### 1. **Python Básico** (`/python/basico/`)
Fundamentals del lenguaje Python que necesitas entender antes de POO.

**Temas cubiertos:**
- Output & Input (print, input)
- Variables y tipos de datos
- Operadores (aritméticos, comparación, lógicos)
- Strings y métodos
- Listas, diccionarios, tuplas
- Control de flujo (if, for, while)
- Funciones y argumentos
- Comprehensions
- Manejo de archivos
- Excepciones

**Ejemplos:** 137 archivos ejecutables

### 2. **Python POO** (`/python/poo/`)
Programación Orientada a Objetos - el siguiente nivel después de dominat los conceptos básicos.

**Temas cubiertos:**
- Clases y objetos
- Atributos (instancia y clase)
- Métodos (instancia, clase, estáticos)
- Propiedades y encapsulamiento
- Herencia (simple, múltiple)
- Polimorfismo
- Métodos especiales (__str__, __repr__, etc)
- Composición
- Patrones de diseño (Singleton, Factory, etc)
- Dataclasses
- Type hints

**Ejemplos:** 39 archivos ejecutables

---

## Flujo de Aprendizaje Recomendado

```
1. Python Básico
   ├─ Output & Variables (necesario para todo)
   ├─ Tipos y Operadores (base de datos)
   ├─ Strings & Listas (estructuras simples)
   ├─ Control de Flujo (lógica)
   ├─ Funciones (reutilización)
   └─ Excepciones (robustez)

2. Python POO
   ├─ Conceptos Fundamentales (class, __init__, self)
   ├─ Métodos (instancia, clase, estático)
   ├─ Propiedades (encapsulamiento)
   ├─ Herencia (reutilización de código)
   ├─ Polimorfismo (flexibilidad)
   ├─ Métodos Especiales (magia en Python)
   ├─ Composición (relaciones entre objetos)
   └─ Patrones (soluciones probadas)
```

---

## Cómo Usar Esta Guía

### Para Aprender un Concepto:
1. Abre el archivo correspondiente en `/examples/`
2. Lee el docstring con objetivo y referencia
3. Ejecuta el código
4. Modifica y experimenta
5. Consulta el `README.md` para contexto

### Para Recordar Rápidamente:
1. Abre el `README.md` de la sección
2. Busca el concepto en la tabla
3. Haz clic en "ver" para ir al ejemplo
4. Ejecuta y copia lo que necesitas

### Ejemplos de Búsqueda:
- "¿Cómo ordeno una lista?" → Busca en Básico > Listas > sorted
- "¿Cómo creo una clase?" → Abre POO > Conceptos Fundamentales > clase_definir__class.py
- "¿Cómo uso @property?" → POO > Propiedades > propiedad_property__property.py

---

## Próximas Expansiones Planificadas

- [ ] Python Avanzado (decoradores, context managers, generators)
- [ ] Python Web (Flask/Django)
- [ ] Python Data Science (NumPy, Matplotlib)
- [ ] Patrones de Diseño Avanzados
- [ ] Testing y Debugging

---

## Estadísticas

| Sección | Archivos | Conceptos | Estado |
|---------|----------|-----------|--------|
| Básico | 137 | 70+ | ✅ Completo |
| POO | 39 | 40+ | ✅ Completo |
| **Total** | **176** | **110+** | ✅ |

---

## Notas Importantes

- Todos los ejemplos son 100% ejecutables
- No requieren dependencias externas (Python standard library)
- Cada archivo enfoca UN concepto
- Output documentado en comentarios
- Compatible con Python 3.7+

Creado con fines educativos. 📚
