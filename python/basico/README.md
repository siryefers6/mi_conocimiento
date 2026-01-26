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

### Enteros (`int`)
| Concepto         | Referencia | Tipo     | Uso                    | Ejemplo                                         |
| ---------------- | ---------- | -------- | ---------------------- | ----------------------------------------------- |
| Asignar variable | `=`        | operador | Asignación de valor    | [ver](examples/asignar_variable__asignacion.py) |
| Conversión       | `int()`    | funcion  | Convertir a entero     | [ver](examples/convertir_tipo__casting.py)      |
| Valor absoluto   | `abs()`    | funcion  | Obtener valor absoluto | [ver](examples/valor_absoluto__abs.py)          |
| Redondeo         | `round()`  | funcion  | Redondear número       | [ver](examples/redondear__round.py)             |

### Flotantes (`float`)
| Concepto         | Referencia | Tipo     | Uso                    | Ejemplo                                         |
| ---------------- | ---------- | -------- | ---------------------- | ----------------------------------------------- |
| Asignar variable | `=`        | operador | Asignación de valor    | [ver](examples/asignar_variable__asignacion.py) |
| Conversión       | `float()`  | funcion  | Convertir a decimal    | [ver](examples/convertir_tipo__casting.py)      |
| Valor absoluto   | `abs()`    | funcion  | Obtener valor absoluto | [ver](examples/valor_absoluto__abs.py)          |
| Redondeo         | `round()`  | funcion  | Redondear número       | [ver](examples/redondear__round.py)             |

### Cadenas (`str`)
| Concepto         | Referencia | Tipo     | Uso                           | Ejemplo                                         |
| ---------------- | ---------- | -------- | ----------------------------- | ----------------------------------------------- |
| Asignar variable | `=`        | operador | Asignación de valor           | [ver](examples/asignar_variable__asignacion.py) |
| Conversión       | `str()`    | funcion  | Convertir a cadena            | [ver](examples/convertir_tipo__casting.py)      |
| Limpiar texto    | `strip()`  | metodo   | Quitar espacios inicial/final | [ver](examples/limpiar_string__strip.py)        |
| Dividir texto    | `split()`  | metodo   | Separar string en lista       | [ver](examples/dividir_strings__split.py)       |
| Unir texto       | `join()`   | metodo   | Concatenar lista en string    | [ver](examples/concatenar_strings__join.py)     |

### Booleanos (`bool`)
| Concepto         | Referencia | Tipo     | Uso                  | Ejemplo                                         |
| ---------------- | ---------- | -------- | -------------------- | ----------------------------------------------- |
| Asignar variable | `=`        | operador | Asignación de valor  | [ver](examples/asignar_variable__asignacion.py) |
| Conversión       | `bool()`   | funcion  | Convertir a booleano | [ver](examples/conversion_bool__bool.py)        |

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
| Iterar rango | `for` | keyword | Iterar sobre una secuencia numérica con `range()` | [ver](examples/iterar_rango__for.py) |
| Iterar diccionario | `for` | keyword | Iterar sobre claves y valores de un diccionario | [ver](examples/iterar_diccionario__for.py) |
| Iterar con índice | `for` | keyword | Iterar con índice usando `enumerate()` | [ver](examples/iterar_con_indice__for.py) |
| Bucle en una línea | `for` | keyword | One-liner para listas o expresiones | [ver](examples/for_inline__for.py) |
| Bucle       | `while`    | keyword | Iteración condicional | [ver](examples/bucle_condicional__while.py) |

---

## Estructuras de datos

### Listas
| Concepto     | Referencia | Tipo   | Uso               | Ejemplo                                          |
| ------------ | ---------- | ------ | ----------------- | ------------------------------------------------ |
| Agregar elemento        | `append`  | metodo | Agregar al final          | [ver](examples/agregar_elemento__list_append.py)    |
| Insertar elemento       | `insert`  | metodo | Insertar en posición      | [ver](examples/insertar_elemento__list_insert.py)   |
| Agregar múltiples       | `extend`  | metodo | Extender lista            | [ver](examples/extender_lista__list_extend.py)      |
| Eliminar por valor      | `remove`  | metodo | Borrar elemento específico| [ver](examples/eliminar_valor__list_remove.py)      |
| Eliminar por índice     | `pop`     | metodo | Borrar por posición       | [ver](examples/eliminar_indice__list_pop.py)        |
| Vaciar lista            | `clear`   | metodo | Eliminar todos los elementos | [ver](examples/vaciar_lista__list_clear.py)     |
| Buscar índice           | `index`   | metodo | Encontrar posición        | [ver](examples/buscar_indice__list_index.py)       |
| Contar ocurrencias      | `count`   | metodo | Contar elementos          | [ver](examples/contar_elementos__list_count.py)    |
| Ordenar lista           | `sort`    | metodo | Ordenar elementos         | [ver](examples/ordenar_lista__list_sort.py)        |
| Invertir lista          | `reverse` | metodo | Dar vuelta a la lista     | [ver](examples/invertir_lista__list_reverse.py)    |
| Copiar lista            | `copy`    | metodo | Crear copia superficial   | [ver](examples/copiar_lista__list_copy.py)         |

### Tuplas
| Concepto     | Referencia | Tipo   | Uso               | Ejemplo                                          |
| ------------ | ---------- | ------ | ----------------- | ------------------------------------------------ |
| Crear tupla                | `tuple`   | clase | Construir tupla          | [ver](examples/crear_tupla__tuple.py)               |
| Contar elementos           | `count`   | metodo| Contar ocurrencias       | [ver](examples/contar_elementos__tuple_count.py)    |
| Buscar índice de valor     | `index`   | metodo| Encontrar posición       | [ver](examples/buscar_indice__tuple_index.py)       |
| Longitud                   | `len`     | funcion| Número de elementos      | [ver](examples/longitud__len.py)                    |
| Suma de elementos          | `sum`     | funcion| Total de elementos numéricos | [ver](examples/suma_elementos__sum.py)         |
| Valor máximo / mínimo      | `max / min` | funcion| Obtener el mayor o menor | [ver](examples/max_min__tuple.py)                  |

### Sets
| Concepto     | Referencia | Tipo   | Uso               | Ejemplo                                          |
| ------------ | ---------- | ------ | ----------------- | ------------------------------------------------ |
| Agregar elemento              | `add`         | metodo| Añadir un elemento al set            | [ver](examples/agregar_elemento__set_add.py)       |
| Eliminar elemento (error)     | `remove`      | metodo| Borrar elemento, lanza error si no existe | [ver](examples/eliminar_elemento__set_remove.py) |
| Eliminar elemento seguro      | `discard`     | metodo| Borrar elemento sin error           | [ver](examples/eliminar_elemento__set_discard.py) |
| Eliminar elemento arbitrario  | `pop`         | metodo| Extraer y eliminar un elemento      | [ver](examples/eliminar_elemento__set_pop.py)     |
| Vaciar set                    | `clear`       | metodo| Eliminar todos los elementos        | [ver](examples/vaciar_set__set_clear.py)          |
| Unión de sets                 | `union`       | metodo| Combinar elementos únicos de dos sets | [ver](examples/union_sets__set_union.py)       |
| Intersección de sets          | `intersection`| metodo| Elementos comunes entre sets        | [ver](examples/interseccion_sets__set_intersection.py) |
| Diferencia de sets            | `difference`  | metodo| Elementos de un set que no están en otro | [ver](examples/diferencia_sets__set_difference.py) |
| Subconjunto                   | `issubset`    | metodo| Verificar si es subconjunto         | [ver](examples/subconjunto__set_issubset.py)      |
| Superconjunto                 | `issuperset`  | metodo| Verificar si es superconjunto       | [ver](examples/superconjunto__set_issuperset.py)  |

### Diccionarios
| Concepto     | Referencia | Tipo   | Uso               | Ejemplo                                          |
| ------------ | ---------- | ------ | ----------------- | ------------------------------------------------ |
| Acceso seguro                 | `get`          | metodo| Obtener valor sin error si no existe | [ver](examples/acceder_diccionario__dict_get.py)     |
| Obtener claves                | `keys`         | metodo| Listar todas las claves               | [ver](examples/obtener_claves__dict_keys.py)        |
| Obtener valores               | `values`       | metodo| Listar todos los valores              | [ver](examples/obtener_valores__dict_values.py)     |
| Obtener pares clave-valor     | `items`        | metodo| Listar tuplas (clave, valor)         | [ver](examples/obtener_items__dict_items.py)        |
| Actualizar diccionario        | `update`       | metodo| Agregar o modificar pares             | [ver](examples/actualizar_diccionario__dict_update.py) |
| Eliminar por clave            | `pop`          | metodo| Borrar y retornar valor               | [ver](examples/eliminar_por_clave__dict_pop.py)     |
| Eliminar elemento arbitrario  | `popitem`      | metodo| Quitar un par cualquiera              | [ver](examples/eliminar_arbitrario__dict_popitem.py)|
| Vaciar diccionario            | `clear`        | metodo| Eliminar todos los pares              | [ver](examples/vaciar_diccionario__dict_clear.py)   |
| Copiar diccionario            | `copy`         | metodo| Copia superficial del diccionario    | [ver](examples/copiar_diccionario__dict_copy.py)    |
| Obtener valor o asignar       | `setdefault`   | metodo| Obtener valor o asignar si no existe | [ver](examples/setdefault_diccionario__dict_setdefault.py) |

---

## Funciones básicas

| Concepto                | Referencia   | Tipo     | Uso                                   | Ejemplo                                              |
|-------------------------|-------------|---------|--------------------------------------|-----------------------------------------------------|
| Longitud                | `len`       | funcion | Obtener número de elementos          | [ver](examples/longitud__len.py)                   |
| Suma de elementos       | `sum`       | funcion | Sumar valores numéricos              | [ver](examples/suma_elementos__sum.py)            |
| Valor máximo / mínimo   | `max / min` | funcion | Obtener mayor o menor valor          | [ver](examples/max_min__tuple.py)                  |
| Valor absoluto          | `abs`       | funcion | Obtener valor absoluto               | [ver](examples/valor_absoluto__abs.py)             |
| Redondeo                | `round`     | funcion | Redondear un número                  | [ver](examples/redondear__round.py)                |
| Aplicar función         | `map`       | funcion | Aplicar función a todos los elementos | [ver](examples/aplicar_funcion__map.py)           |
| Filtrar elementos       | `filter`    | funcion | Filtrar elementos según condición    | [ver](examples/filtrar_elementos__filter.py)       |
| Combinar secuencias     | `zip`       | funcion | Combinar iterables en tuplas         | [ver](examples/combinar_secuencias__zip.py)       |
| Iterar con índice       | `enumerate` | funcion | Obtener índice y valor en iteración | [ver](examples/iterar_con_indice__enumerate.py)   |
| Ordenar secuencia       | `sorted`    | funcion | Devolver lista ordenada              | [ver](examples/ordenar_lista__sorted.py)          |
| Todos / Alguno          | `all / any` | funcion | Verificar condición en todos o alguno | [ver](examples/verificar_condicion__all_any.py)  |
| Concatenar strings      | `join`      | metodo  | Unir elementos de una lista en string | [ver](examples/concatenar_strings__join.py)      |
| Dividir strings         | `split`     | metodo  | Separar una cadena en lista usando un separador | [ver](examples/dividir_strings__split.py) |
| Limpiar string          | `strip`     | metodo  | Eliminar espacios u otros caracteres al inicio y final | [ver](examples/limpiar_string__strip.py) |

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
| Capturar error como variable    | `try/except as e`  | keyword | Inspeccionar el error                       | [ver](examples/capturar_error_as__try_except.py)   |
| Capturar errores específicos    | `except <Error>`   | keyword | Manejar distintos tipos de excepciones     | [ver](examples/capturar_error_especifico__try_except.py) |
| Try/except con else             | `try/except/else`  | keyword | Ejecutar código si no hay excepción        | [ver](examples/try_except_con_else__try_except.py) |
| Try/finally                     | `try/finally`      | keyword | Ejecutar siempre un bloque de código       | [ver](examples/try_finally__try_except.py)        |
| Re-lanzar excepciones           | `raise`            | keyword | Propagar el error a niveles superiores     | [ver](examples/re_lanzar_error__try_except.py)    |

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
