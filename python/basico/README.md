# Python Básico

Conjunto de ejemplos ejecutables que cubren el **80/20** del lenguaje Python.

El objetivo es resolver problemas reales con la menor cantidad de conceptos posibles.

---

## Estructura

* Este README **indexa** el conocimiento.
* Cada ejemplo vive en `examples/`.
* Cada archivo resuelve **un solo problema**.

---

## Entrada y salida

| Concepto       | Referencia | Tipo    | Uso                 | Ejemplo                                  |
| -------------- | ---------- | ------- | ------------------- | ---------------------------------------- |
| Imprimir texto | `print`    | funcion | Salida estándar     | [ver](examples/imprimir_texto__print.py) |
| Leer entrada   | `input`    | funcion | Entrada del usuario | [ver](examples/leer_entrada__input.py)   |

---

## Variables y tipos

| Concepto            | Referencia | Tipo     | Uso                 | Ejemplo                                         |
| ------------------- | ---------- | -------- | ------------------- | ----------------------------------------------- |
| Asignar variable    | `=`        | operador | Asignación de valor | [ver](examples/asignar_variable__asignacion.py) |
| Ver tipo            | `type`     | funcion  | Inspección de tipo  | [ver](examples/ver_tipo__type.py)               |
| Conversión de tipos | `int`      | funcion  | Casting explícito   | [ver](examples/convertir_tipo__casting.py)      |

---

## Operadores

| Concepto    | Referencia   | Tipo     | Uso                   | Ejemplo                                           |
| ----------- | ------------ | -------- | --------------------- | ------------------------------------------------- |
| Aritméticos | `+ - * / % **`    | operador | Operaciones numéricas | [ver](examples/operadores_aritmeticos__basico.py) |
| Comparación | `== != > <`  | operador | Comparar valores      | [ver](examples/operadores_comparacion__basico.py) |
| Lógicos     | `and or not` | keyword  | Expresiones booleanas | [ver](examples/operadores_logicos__basico.py)     |

---

## Control de flujo

| Concepto    | Referencia | Tipo    | Uso                   | Ejemplo                                     |
| ----------- | ---------- | ------- | --------------------- | ------------------------------------------- |
| Condicional | `if`       | keyword | Decisiones            | [ver](examples/control_flujo__if.py)        |
| Condicional alternativa | `if / else` | keyword | Rama alternativa | [ver](examples/if_else__if.py) |
| Múltiples condiciones | `if / elif / else` | keyword | Varias ramas | [ver](examples/if_elif_else__if.py) |
| Condición compuesta | `if` | keyword | and / or | [ver](examples/if_condicion_compuesta__if.py) |
| Validación temprana | `if` | keyword | Guard clause | [ver](examples/if_guard_clause__if.py) |
| Condicional inline | `if` | keyword | Condicional en una sola línea (one-liner) | [ver](examples/if_inline__if.py) |
| Bucle       | `for`      | keyword | Iterar secuencias     | [ver](examples/iterar_secuencia__for.py)    |
| Bucle       | `while`    | keyword | Iteración condicional | [ver](examples/bucle_condicional__while.py) |

---

## Estructuras de datos

| Concepto     | Referencia | Tipo   | Uso               | Ejemplo                                          |
| ------------ | ---------- | ------ | ----------------- | ------------------------------------------------ |
| Listas       | `append`   | metodo | Agregar elementos | [ver](examples/agregar_elemento__list_append.py) |
| Tuplas       | `tuple`    | clase  | Datos inmutables  | [ver](examples/crear_tupla__tuple.py)            |
| Sets         | `add`      | metodo | Elementos únicos  | [ver](examples/agregar_elemento__set_add.py)     |
| Diccionarios | `get`      | metodo | Acceso seguro     | [ver](examples/acceder_diccionario__dict_get.py) |

---

## Funciones

| Concepto        | Referencia | Tipo     | Uso               | Ejemplo                                        |
| --------------- | ---------- | -------- | ----------------- | ---------------------------------------------- |
| Definir función | `def`      | keyword  | Reutilizar lógica | [ver](examples/definir_funcion__def.py)        |
| Parámetros      | argumentos | concepto | Entrada de datos  | [ver](examples/funcion_con_parametros__def.py) |
| Retorno         | `return`   | keyword  | Devolver valores  | [ver](examples/retornar_valor__return.py)      |

---

## Manejo de errores

| Concepto       | Referencia   | Tipo    | Uso          | Ejemplo                                      |
| -------------- | ------------ | ------- | ------------ | -------------------------------------------- |
| Capturar error | `try/except` | keyword | Evitar crash | [ver](examples/manejar_error__try_except.py) |

---

## Estilo y utilidades

| Concepto          | Referencia | Tipo       | Uso                        | Ejemplo                                          |
| ----------------- | ---------- | ---------- | -------------------------- | ------------------------------------------------ |
| Comentarios       | `#`        | operador   | Documentar código          | [ver](examples/comentar_codigo__comentarios.py)  |
| Docstrings        | `""" """`  | sintaxis   | Documentar funciones       | [ver](examples/documentar_funcion__docstring.py) |
| Convención Google | docstring  | convencion | Estandarizar documentación | [ver](examples/docstring_google__estilo.py)      |
| Ayuda integrada   | `help`     | funcion    | Consultar documentación    | [ver](examples/usar_help__help.py)               |

---

## Regla final

Si un ejemplo no se entiende en **30 segundos**, debe simplificarse.

Este módulo cumple la regla **80/20** y sirve como base para cualquier librería o framework.
