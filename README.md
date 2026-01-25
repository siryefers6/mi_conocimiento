# Knowledge Base

Base de conocimiento técnico orientada a **consulta rápida**, **ejemplos ejecutables** y **crecimiento progresivo**.

El repositorio no es un tutorial narrativo. Es un **sistema de referencia** organizado por problemas reales y soluciones concretas.

---

## 1. Principios del diseño

* Un ejemplo resuelve **un solo problema**.
* Un archivo demuestra **un solo uso** de un método.
* El README **indexa**, los archivos **explican y ejecutan**.
* El contexto vive en la **estructura de carpetas**, no en las tablas.
* Todo el código debe ser **reproducible**.

---

## 2. Cómo se construye el conocimiento

El conocimiento se organiza por capas:

1. **Lenguaje** (python, javascript, sql)
2. **Dominio / librería** (basico, pandas, react)
3. **Problema técnico** (filtrar filas, agrupar datos)
4. **Ejemplo ejecutable**

Cada capa reduce ambigüedad y mejora la búsqueda.

---

## 3. Estructura de ficheros

```text
knowledge-base/
├── README.md
├── python/
│   ├── basico/
│   │   ├── README.md
│   │   └── examples/
│   └── pandas/
│       ├── README.md
│       └── examples/
├── javascript/
│   └── basico/
└── sql/
```

Reglas:

* Un `README.md` por dominio.
* Carpeta `examples/` obligatoria.
* Enlaces siempre **relativos**.

---

## 4. Tabla simplificada (por dominio)

Cada `README.md` de dominio contiene una tabla mínima.

```md
| Concepto | Método | Uso | Ejemplo |
|--------|--------|-----|---------|
| Filtrar filas | `loc` | Filtro por condición | [ver](examples/filtrar_filas__loc.py) |
| Agrupar datos | `groupby` | Agregación | [ver](examples/agrupar_datos__groupby.py) |
```

Definiciones:

* **Concepto**: problema técnico
* **Método**: API / keyword (siempre en backticks)
* **Uso**: intención concreta
* **Ejemplo**: archivo ejecutable

---

## 5. Convención de nombres de archivos

### Patrón obligatorio

```text
<accion>_<contexto>__<metodo>.py
```

Ejemplos válidos:

* `filtrar_filas__loc.py`
* `agrupar_datos__groupby_agg.py`
* `iterar_listas__for.py`

Beneficios:

* Búsqueda inmediata
* Escala a cualquier lenguaje
* Evita nombres ambiguos

---

## 6. Formato estándar de los ejemplos

Todos los ejemplos deben seguir esta plantilla.

```python
"""
Objetivo: problema concreto que se resuelve
Método: API / keyword principal
Dataset: archivo(s) usados
Nivel: basico | intermedio | avanzado
"""

# imports

# carga de datos

# transformación

# resultado
```

Reglas:

* Comentarios mínimos y técnicos
* Una sola responsabilidad
* Resultado visible (`print`, `return`)

---

## 7. Qué NO debe contener un ejemplo

* Teoría extensa
* Explicaciones narrativas
* Múltiples métodos mezclados
* Código no ejecutable

---

## 8. Regla de diseño clave

> **Un método puede tener múltiples usos, pero cada uso vive en su propio archivo.**

La tabla tiene múltiples filas.
Los ejemplos son siempre atómicos.

---

## 9. Escalabilidad

Este diseño permite:

* Añadir nuevos lenguajes
* Añadir nuevas librerías
* Búsqueda semántica por problema
* Migración futura a SQL / Docs / Wiki

---

## 10. Regla final

Si un ejemplo no se entiende en **30 segundos**, debe simplificarse.

Este repositorio prioriza **claridad, precisión y reutilización**.
