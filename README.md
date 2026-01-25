# Knowledge Base

Base de conocimiento técnico orientada a **consulta rápida**, **ejemplos ejecutables** y **crecimiento progresivo**.

El repositorio no es un tutorial narrativo. Es un **sistema de referencia** organizado por problemas reales y soluciones concretas.

---

## 1. Principios del diseño

* Un ejemplo resuelve **un solo problema**.
* Un archivo demuestra **un solo uso** de una referencia.
* El README **indexa**, los archivos **explican y ejecutan**.
* El contexto vive en la **estructura de carpetas**, no en las tablas.
* Todo el código debe ser **reproducible**.

---

## 2. Cómo se construye el conocimiento

El conocimiento se organiza por capas:

1. **Lenguaje** (python, javascript, sql)
2. **Dominio** (basico, pandas, react)
3. **Problema técnico** (filtrar filas, imprimir texto)
4. **Referencia técnica** (función, método, keyword, operador)
5. **Ejemplo ejecutable**

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
| Concepto | Referencia | Tipo | Uso | Ejemplo |
|--------|-----------|------|-----|---------|
| Imprimir texto | `print` | función | Salida estándar | [ver](examples/imprimir_texto__print.py) |
| Condicional | `if` | keyword | Control de flujo | [ver](examples/control_flujo__if.py) |
```

Definiciones:

* **Concepto**: problema técnico
* **Referencia**: función, método, keyword, operador, clase o módulo (siempre en backticks)
* **Tipo**: naturaleza de la referencia
* **Uso**: intención concreta
* **Ejemplo**: archivo ejecutable

Tipos válidos:

* función
* método
* keyword
* operador
* clase
* módulo

---

## 5. Convención de nombres de archivos

### Patrón obligatorio

```text
<accion>_<contexto>__<referencia>.py
```

Ejemplos válidos:

* `imprimir_texto__print.py`
* `control_flujo__if.py`
* `agrupar_datos__groupby.py`

---

## 6. Formato estándar de los ejemplos

Todos los ejemplos deben seguir esta plantilla.

```python
"""
Objetivo: problema concreto que se resuelve
Referencia: función / keyword / método
Tipo: funcion | metodo | keyword | operador | clase | modulo
Nivel: basico | intermedio | avanzado
"""

# imports

# carga de datos

# transformación

# resultado
print(resultado)

"""output
salida esperada de la ejecución
"""
```

Reglas:

* El bloque `"""output` documenta el **resultado real** del script
* Mantén el output corto y representativo
* No simules resultados irreales
* Una sola responsabilidad por archivo

---

## 7. Qué NO debe contener un ejemplo

* Teoría extensa
* Explicaciones narrativas
* Múltiples referencias mezcladas
* Código no ejecutable

---

## 8. Regla de diseño clave

> **Una referencia puede tener múltiples usos, pero cada uso vive en su propio archivo.**

La tabla tiene múltiples filas.
Los ejemplos son siempre atómicos.

---

## 9. YAML de indexación (opcional)

Si se usa YAML para indexar ejemplos:

```yaml
concepto: Imprimir texto
referencia: print
tipo: funcion
uso: Salida estándar
nivel: basico
lenguaje: python
dominio: basico
ejemplo: examples/imprimir_texto__print.py
```

---

## 10. Regla final

Si un ejemplo no se entiende en **30 segundos**, debe simplificarse.

Este repositorio prioriza **claridad, precisión y reutilización**.
