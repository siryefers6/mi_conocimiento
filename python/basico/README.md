# Python Básico - Guía Completa

Referencia rápida de conceptos fundamentales, funciones y operadores de Python con ejemplos ejecutables.

---

## Output y Entrada

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Imprimir texto | `print()` | función | Salida estándar | [ver](examples/output_texto__print.py) |
| Imprimir múltiples valores | `print()` | función | Múltiples argumentos | [ver](examples/output_multiples__print.py) |
| Entrada del usuario | `input()` | función | Leer desde teclado | [ver](examples/entrada_usuario__input.py) |
| Entrada con tipo | `int(input())` | función | Convertir entrada | [ver](examples/entrada_convertir__int.py) |

---

## Variables y Asignación

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Asignar variable | `=` | operador | Crear variable | [ver](examples/variable_asignar__asignacion.py) |
| Múltiple asignación | `=` | operador | Asignar varios valores | [ver](examples/variable_multiple__asignacion.py) |
| Cambiar valor | `=` | operador | Modificar variable | [ver](examples/variable_modificar__asignacion.py) |
| Incrementar variable | `+=` | operador | Sumar y asignar | [ver](examples/variable_incrementar__operador.py) |

---

## Tipos de Datos Básicos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Entero (int) | `int` | tipo | Números sin decimales | [ver](examples/tipo_entero__int.py) |
| Decimal (float) | `float` | tipo | Números con decimales | [ver](examples/tipo_decimal__float.py) |
| Texto (str) | `str` | tipo | Cadenas de caracteres | [ver](examples/tipo_texto__str.py) |
| Booleano (bool) | `bool` | tipo | Verdadero o falso | [ver](examples/tipo_booleano__bool.py) |
| Tipo de variable | `type()` | función | Identificar el tipo | [ver](examples/tipo_identificar__type.py) |
| Convertir a entero | `int()` | función | Conversión a int | [ver](examples/tipo_convertir__int.py) |
| Convertir a decimal | `float()` | función | Conversión a float | [ver](examples/tipo_convertir__float.py) |
| Convertir a texto | `str()` | función | Conversión a string | [ver](examples/tipo_convertir__str.py) |

---

## Operadores Aritméticos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Suma | `+` | operador | Adición | [ver](examples/operador_suma__suma.py) |
| Resta | `-` | operador | Sustracción | [ver](examples/operador_resta__resta.py) |
| Multiplicación | `*` | operador | Multiplicación | [ver](examples/operador_multiplicacion__mult.py) |
| División | `/` | operador | División con decimales | [ver](examples/operador_division__div.py) |
| División entera | `//` | operador | División sin decimales | [ver](examples/operador_division_entera__floordiv.py) |
| Módulo | `%` | operador | Resto de división | [ver](examples/operador_modulo__mod.py) |
| Potencia | `**` | operador | Elevar a potencia | [ver](examples/operador_potencia__pow.py) |

---

## Operadores de Comparación

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Igual que | `==` | operador | Igualdad | [ver](examples/comparacion_igual__eq.py) |
| No igual que | `!=` | operador | Desigualdad | [ver](examples/comparacion_no_igual__ne.py) |
| Mayor que | `>` | operador | Mayor a | [ver](examples/comparacion_mayor__gt.py) |
| Menor que | `<` | operador | Menor a | [ver](examples/comparacion_menor__lt.py) |
| Mayor o igual | `>=` | operador | Mayor o igual | [ver](examples/comparacion_mayor_igual__ge.py) |
| Menor o igual | `<=` | operador | Menor o igual | [ver](examples/comparacion_menor_igual__le.py) |

---

## Operadores Lógicos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Y (AND) | `and` | operador | Ambas condiciones | [ver](examples/logico_and__and.py) |
| O (OR) | `or` | operador | Cualquier condición | [ver](examples/logico_or__or.py) |
| NO (NOT) | `not` | operador | Invertir lógica | [ver](examples/logico_not__not.py) |

---

## Strings (Cadenas de Texto)

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear string | `""` o `''` | literal | Texto entre comillas | [ver](examples/string_crear__comillas.py) |
| Concatenación | `+` | operador | Unir strings | [ver](examples/string_concatenar__suma.py) |
| Repetición | `*` | operador | Repetir string | [ver](examples/string_repetir__mult.py) |
| Largo del string | `len()` | función | Número de caracteres | [ver](examples/string_largo__len.py) |
| Mayúsculas | `upper()` | método | Convertir a mayúsculas | [ver](examples/string_mayusculas__upper.py) |
| Minúsculas | `lower()` | método | Convertir a minúsculas | [ver](examples/string_minusculas__lower.py) |
| Primera letra capital | `capitalize()` | método | Capitalizar | [ver](examples/string_capitalizar__capitalize.py) |
| Reemplazar texto | `replace()` | método | Sustituir contenido | [ver](examples/string_reemplazar__replace.py) |
| Dividir string | `split()` | método | Partir en lista | [ver](examples/string_dividir__split.py) |
| Unir lista en string | `join()` | método | Concatenar lista | [ver](examples/string_unir__join.py) |
| Buscar posición | `find()` | método | Localizar substring | [ver](examples/string_posicion__find.py) |
| Verificar contenido | `in` | operador | Comprobar substring | [ver](examples/string_contiene__in.py) |
| Indización | `[]` | operador | Acceder a carácter | [ver](examples/string_indizar__indexacion.py) |
| Slicing | `[:]` | operador | Obtener porción | [ver](examples/string_slice__slicing.py) |
| F-strings | `f""` | literal | Formato interpolado | [ver](examples/string_fstring__fstring.py) |

---

## Listas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear lista | `[]` | literal | Lista vacía | [ver](examples/lista_crear__brackets.py) |
| Crear con valores | `[]` | literal | Lista con elementos | [ver](examples/lista_elementos__brackets.py) |
| Acceder elemento | `[]` | operador | Obtener por índice | [ver](examples/lista_acceder__indexacion.py) |
| Modificar elemento | `[]` | operador | Cambiar valor en índice | [ver](examples/lista_modificar__asignacion.py) |
| Largo de lista | `len()` | función | Número de elementos | [ver](examples/lista_largo__len.py) |
| Agregar elemento | `append()` | método | Añadir al final | [ver](examples/lista_agregar__append.py) |
| Insertar en posición | `insert()` | método | Insertar en índice | [ver](examples/lista_insertar__insert.py) |
| Eliminar por índice | `pop()` | método | Sacar y remover | [ver](examples/lista_eliminar__pop.py) |
| Eliminar por valor | `remove()` | método | Remover primer match | [ver](examples/lista_remover__remove.py) |
| Limpiar lista | `clear()` | método | Vaciar lista | [ver](examples/lista_limpiar__clear.py) |
| Contar elemento | `count()` | método | Número de ocurrencias | [ver](examples/lista_contar__count.py) |
| Encontrar índice | `index()` | método | Posición de elemento | [ver](examples/lista_indice__index.py) |
| Ordenar lista | `sort()` | método | Orden ascendente | [ver](examples/lista_ordenar__sort.py) |
| Invertir lista | `reverse()` | método | Orden inverso | [ver](examples/lista_invertir__reverse.py) |
| Copiar lista | `copy()` | método | Copia superficial | [ver](examples/lista_copiar__copy.py) |
| Slicing | `[:]` | operador | Obtener porción | [ver](examples/lista_slice__slicing.py) |
| Verificar elemento | `in` | operador | Elemento existe | [ver](examples/lista_contiene__in.py) |

---

## Diccionarios

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear diccionario | `{}` | literal | Dict vacío | [ver](examples/dict_crear__braces.py) |
| Con pares clave-valor | `{}` | literal | Dict con datos | [ver](examples/dict_pares__braces.py) |
| Acceder valor | `[]` | operador | Obtener por clave | [ver](examples/dict_acceder__indexacion.py) |
| Acceder con get | `get()` | método | Acceso seguro | [ver](examples/dict_get__get.py) |
| Asignar valor | `[]` | operador | Crear/cambiar clave | [ver](examples/dict_asignar__indexacion.py) |
| Eliminar clave | `pop()` | método | Remover y devolver | [ver](examples/dict_eliminar__pop.py) |
| Limpiar dict | `clear()` | método | Vaciar diccionario | [ver](examples/dict_limpiar__clear.py) |
| Obtener claves | `keys()` | método | Lista de claves | [ver](examples/dict_claves__keys.py) |
| Obtener valores | `values()` | método | Lista de valores | [ver](examples/dict_valores__values.py) |
| Obtener pares | `items()` | método | Lista de tuplas | [ver](examples/dict_items__items.py) |
| Verificar clave | `in` | operador | Clave existe | [ver](examples/dict_contiene__in.py) |
| Número elementos | `len()` | función | Cantidad de pares | [ver](examples/dict_largo__len.py) |

---

## Tuplas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear tupla | `()` | literal | Tupla vacía | [ver](examples/tupla_crear__parentesis.py) |
| Con elementos | `()` | literal | Tupla con datos | [ver](examples/tupla_elementos__parentesis.py) |
| Tupla de un elemento | `()` | literal | Un elemento + coma | [ver](examples/tupla_un_elemento__parentesis.py) |
| Acceder elemento | `[]` | operador | Obtener por índice | [ver](examples/tupla_acceder__indexacion.py) |
| Largo de tupla | `len()` | función | Número de elementos | [ver](examples/tupla_largo__len.py) |
| Contar ocurrencias | `count()` | método | Repeticiones de valor | [ver](examples/tupla_contar__count.py) |
| Encontrar índice | `index()` | método | Posición de elemento | [ver](examples/tupla_indice__index.py) |
| Slicing | `[:]` | operador | Obtener porción | [ver](examples/tupla_slice__slicing.py) |
| Verificar elemento | `in` | operador | Elemento existe | [ver](examples/tupla_contiene__in.py) |

---

## Control de Flujo - Condicionales

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Si (if) | `if` | keyword | Ejecutar si es verdadero | [ver](examples/condicional_if__if.py) |
| Si no (else) | `else` | keyword | Alternativa a if | [ver](examples/condicional_else__else.py) |
| Si no si (elif) | `elif` | keyword | Múltiples condiciones | [ver](examples/condicional_elif__elif.py) |
| Condicional ternario | `if-else` | expresión | Una línea | [ver](examples/condicional_ternario__ternario.py) |

---

## Control de Flujo - Bucles

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Bucle for | `for` | keyword | Iterar sobre secuencia | [ver](examples/bucle_for__for.py) |
| For con range | `range()` | función | Generar números | [ver](examples/bucle_range__range.py) |
| For con enumerate | `enumerate()` | función | Índice y valor | [ver](examples/bucle_enumerate__enumerate.py) |
| For con zip | `zip()` | función | Iterar múltiples listas | [ver](examples/bucle_zip__zip.py) |
| Bucle while | `while` | keyword | Iterar mientras condición | [ver](examples/bucle_while__while.py) |
| Romper bucle | `break` | keyword | Salir del bucle | [ver](examples/bucle_break__break.py) |
| Saltar iteración | `continue` | keyword | Siguiente iteración | [ver](examples/bucle_continue__continue.py) |
| Else en bucle | `else` | keyword | Después del bucle | [ver](examples/bucle_else__else.py) |

---

## Funciones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Definir función | `def` | keyword | Crear función | [ver](examples/funcion_definir__def.py) |
| Retornar valor | `return` | keyword | Devolver resultado | [ver](examples/funcion_retornar__return.py) |
| Múltiples retornos | `return` | keyword | Tupla de valores | [ver](examples/funcion_multiples_retornos__return.py) |
| Parámetro por defecto | `=` | operador | Valor inicial | [ver](examples/funcion_defecto__defecto.py) |
| Args variable | `*args` | parámetro | Argumentos variables | [ver](examples/funcion_args__args.py) |
| Kwargs variable | `**kwargs` | parámetro | Argumentos nombrados | [ver](examples/funcion_kwargs__kwargs.py) |
| Docstring | `"""` | literal | Documentación función | [ver](examples/funcion_docstring__docstring.py) |

---

## Iteración - Comprensiones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| List comprehension | `[x for x in]` | expresión | Crear lista concisa | [ver](examples/iteracion_list_comp__listcomp.py) |
| List comp con condición | `[x for x if]` | expresión | Filtrar mientras crea | [ver](examples/iteracion_list_comp_filtro__listcomp.py) |
| Dict comprehension | `{k:v for}` | expresión | Crear dict conciso | [ver](examples/iteracion_dict_comp__dictcomp.py) |
| Set comprehension | `{x for x in}` | expresión | Crear set conciso | [ver](examples/iteracion_set_comp__setcomp.py) |

---

## Conjuntos (Sets)

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Crear set | `{}` o `set()` | literal/función | Conjunto vacío | [ver](examples/set_crear__set.py) |
| Set con elementos | `{}` | literal | Conjunto de valores | [ver](examples/set_elementos__braces.py) |
| Agregar elemento | `add()` | método | Añadir al set | [ver](examples/set_agregar__add.py) |
| Eliminar elemento | `remove()` | método | Remover elemento | [ver](examples/set_eliminar__remove.py) |
| Largo del set | `len()` | función | Número de elementos | [ver](examples/set_largo__len.py) |
| Verificar elemento | `in` | operador | Elemento existe | [ver](examples/set_contiene__in.py) |
| Unión | `union()` | método | Todos los elementos | [ver](examples/set_union__union.py) |
| Intersección | `intersection()` | método | Elementos comunes | [ver](examples/set_interseccion__intersection.py) |
| Diferencia | `difference()` | método | Elementos únicos | [ver](examples/set_diferencia__difference.py) |

---

## Funciones Integradas Importantes

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Rango de números | `range()` | función | Generar secuencia | [ver](examples/builtin_range__range.py) |
| Máximo valor | `max()` | función | Encontrar mayor | [ver](examples/builtin_max__max.py) |
| Mínimo valor | `min()` | función | Encontrar menor | [ver](examples/builtin_min__min.py) |
| Suma | `sum()` | función | Total de números | [ver](examples/builtin_sum__sum.py) |
| Largo | `len()` | función | Tamaño de secuencia | [ver](examples/builtin_len__len.py) |
| Redondear | `round()` | función | Aproximar número | [ver](examples/builtin_round__round.py) |
| Valor absoluto | `abs()` | función | Número sin signo | [ver](examples/builtin_abs__abs.py) |
| Todos verdaderos | `all()` | función | AND de secuencia | [ver](examples/builtin_all__all.py) |
| Alguno verdadero | `any()` | función | OR de secuencia | [ver](examples/builtin_any__any.py) |
| Ordenar | `sorted()` | función | Listar ordenada | [ver](examples/builtin_sorted__sorted.py) |
| Invertir | `reversed()` | función | Iterar invertido | [ver](examples/builtin_reversed__reversed.py) |
| Aplicar función | `map()` | función | Transformar elementos | [ver](examples/builtin_map__map.py) |
| Filtrar | `filter()` | función | Seleccionar elementos | [ver](examples/builtin_filter__filter.py) |
| Enumerar | `enumerate()` | función | Índice y valor | [ver](examples/builtin_enumerate__enumerate.py) |

---

## Manejo de Archivos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Abrir archivo | `open()` | función | Crear objeto archivo | [ver](examples/archivo_abrir__open.py) |
| Leer todo | `read()` | método | Contenido completo | [ver](examples/archivo_leer__read.py) |
| Leer líneas | `readlines()` | método | Lista de líneas | [ver](examples/archivo_lineas__readlines.py) |
| Leer una línea | `readline()` | método | Siguiente línea | [ver](examples/archivo_readline__readline.py) |
| Escribir | `write()` | método | Escribir contenido | [ver](examples/archivo_escribir__write.py) |
| Cerrar archivo | `close()` | método | Liberar recurso | [ver](examples/archivo_cerrar__close.py) |
| With (context manager) | `with` | keyword | Manejo automático | [ver](examples/archivo_with__with.py) |

---

## Excepciones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Capturar excepción | `try-except` | keyword | Manejar errores | [ver](examples/excepcion_try__try.py) |
| Excepto específica | `except` | keyword | Capturar tipo error | [ver](examples/excepcion_except__except.py) |
| Código limpieza | `finally` | keyword | Después de error o no | [ver](examples/excepcion_finally__finally.py) |
| Lanzar excepción | `raise` | keyword | Generar error | [ver](examples/excepcion_raise__raise.py) |

---

## Notas Importantes

- Un archivo = un concepto
- Todo código debe ser reproducible
- Mantén ejemplos simples y claros
- El output documenta el resultado esperado
