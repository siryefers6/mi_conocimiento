# JavaScript - Básico e Intermedio

Referencia rápida de conceptos, funciones y métodos de JavaScript con ejemplos ejecutables.

---

## Nivel Básico

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Imprimir en consola | `console.log()` | método | Salida estándar | [ver](examples/imprimir_texto__console_log.js) |
| Declarar variable | `let` | keyword | Almacenamiento de datos | [ver](examples/asignar_variable__let.js) |
| Constante | `const` | keyword | Variable inmutable | [ver](examples/asignar_constante__const.js) |
| Condicional simple | `if` | keyword | Control de flujo | [ver](examples/control_flujo__if.js) |
| Condicional doble | `if...else` | keyword | Bifurcación condicional | [ver](examples/if_else__if.js) |
| Múltiples condiciones | `if...else if...else` | keyword | Flujo con múltiples opciones | [ver](examples/if_elif_else__if.js) |
| Bucle de iteración | `for` | keyword | Repetición controlada | [ver](examples/bucle_for__for.js) |
| Bucle mientras | `while` | keyword | Repetición condicional | [ver](examples/bucle_while__while.js) |
| Detener bucle | `break` | keyword | Salir de bucle | [ver](examples/bucle_break__break.js) |
| Saltar iteración | `continue` | keyword | Siguiente iteración | [ver](examples/bucle_continue__continue.js) |
| Función básica | `function` | keyword | Definición de procedimiento | [ver](examples/definir_funcion__function.js) |
| Función anónima | `function () {}` | keyword | Función sin nombre | [ver](examples/funcion_anonima__function.js) |
| Función flecha | `=>` | operador | Sintaxis concisa de función | [ver](examples/funcion_flecha__arrow.js) |
| Retorno de función | `return` | keyword | Devolver valor | [ver](examples/retornar_valor__return.js) |
| Parámetro por defecto | `= valor` | operador | Valor predeterminado | [ver](examples/parametro_defecto__default.js) |
| Array | `[]` | literal | Colección indexada | [ver](examples/crear_array__array.js) |
| Acceder elemento | `array[i]` | operador | Obtener por índice | [ver](examples/acceder_elemento__index.js) |
| Agregar al final | `push()` | método | Insertar al final | [ver](examples/agregar_elemento__push.js) |
| Eliminar del final | `pop()` | método | Extraer último | [ver](examples/eliminar_elemento__pop.js) |
| Eliminar por índice | `splice()` | método | Remover elemento | [ver](examples/eliminar_indice__splice.js) |
| Contar elementos | `length` | propiedad | Tamaño del array | [ver](examples/contar_elementos__length.js) |
| Objeto | `{}` | literal | Colección clave-valor | [ver](examples/crear_objeto__object.js) |
| Acceder propiedad | `objeto.clave` | operador | Obtener por clave | [ver](examples/acceder_propiedad__dot.js) |
| Acceder propiedad dinámica | `objeto[clave]` | operador | Obtener por clave variable | [ver](examples/acceder_dinamico__bracket.js) |
| Asignar propiedad | `objeto.clave = valor` | operador | Establecer propiedad | [ver](examples/asignar_propiedad__dot.js) |
| Iterar array | `for...of` | keyword | Recorrer elemento a elemento | [ver](examples/iterar_array__for_of.js) |
| Iterar objeto | `for...in` | keyword | Recorrer claves | [ver](examples/iterar_objeto__for_in.js) |
| String | `""` o `''` | literal | Cadena de texto | [ver](examples/crear_string__string.js) |
| Template literal | `` ` ` `` | literal | String interpolado | [ver](examples/template_literal__backticks.js) |
| Concatenar strings | `+` | operador | Unir textos | [ver](examples/concatenar_strings__plus.js) |
| Convertir a string | `String()` | función | Casteo de tipo | [ver](examples/convertir_string__String.js) |
| Convertir a número | `Number()` | función | Casteo de tipo | [ver](examples/convertir_numero__Number.js) |
| Parsear número | `parseInt()` | función | Extraer número entero | [ver](examples/parsear_numero__parseInt.js) |
| Booleano | `true / false` | literal | Valor lógico | [ver](examples/crear_booleano__boolean.js) |
| Operador lógico AND | `&&` | operador | Conjunción lógica | [ver](examples/operador_and__and.js) |
| Operador lógico OR | `&#124;&#124;` | operador | Disyunción lógica | [ver](examples/operador_or__or.js) |
| Operador lógico NOT | `!` | operador | Negación lógica | [ver](examples/operador_not__not.js) |
| Comparación igual | `==` | operador | Igualdad flexible | [ver](examples/comparar_igual__double_equal.js) |
| Comparación estricta | `===` | operador | Igualdad estricta | [ver](examples/comparar_estricto__triple_equal.js) |
| Comparación menor | `<` | operador | Menor que | [ver](examples/comparar_menor__less.js) |
| Comparación mayor | `>` | operador | Mayor que | [ver](examples/comparar_mayor__greater.js) |
| Resto/módulo | `%` | operador | Residuo de división | [ver](examples/modulo__remainder.js) |

---

## Nivel Intermedio

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Método `map()` | `array.map()` | método | Transformar cada elemento | [ver](examples/mapear_elementos__map.js) |
| Método `filter()` | `array.filter()` | método | Filtrar elementos | [ver](examples/filtrar_elementos__filter.js) |
| Método `reduce()` | `array.reduce()` | método | Acumular valores | [ver](examples/acumular_valores__reduce.js) |
| Método `find()` | `array.find()` | método | Encontrar primer elemento | [ver](examples/buscar_elemento__find.js) |
| Método `includes()` | `array.includes()` | método | Verificar existencia | [ver](examples/verificar_elemento__includes.js) |
| Método `indexOf()` | `array.indexOf()` | método | Encontrar índice | [ver](examples/buscar_indice__indexOf.js) |
| Método `slice()` | `array.slice()` | método | Extraer sección | [ver](examples/extraer_seccion__slice.js) |
| Método `join()` | `array.join()` | método | Concatenar elementos | [ver](examples/concatenar_array__join.js) |
| Método `split()` | `string.split()` | método | Dividir string | [ver](examples/dividir_string__split.js) |
| Método `trim()` | `string.trim()` | método | Remover espacios | [ver](examples/limpiar_string__trim.js) |
| Método `toUpperCase()` | `string.toUpperCase()` | método | Mayúsculas | [ver](examples/convertir_mayusculas__toUpperCase.js) |
| Método `toLowerCase()` | `string.toLowerCase()` | método | Minúsculas | [ver](examples/convertir_minusculas__toLowerCase.js) |
| Método `replace()` | `string.replace()` | método | Reemplazar texto | [ver](examples/reemplazar_texto__replace.js) |
| Método `includes()` (string) | `string.includes()` | método | Verificar contiene | [ver](examples/verificar_contiene__includes.js) |
| Operador spread | `...` | operador | Desempacar elementos | [ver](examples/spread_operator__spread.js) |
| Desestructuración array | `[a, b] = array` | keyword | Extraer valores | [ver](examples/desestructurar_array__destructure.js) |
| Desestructuración objeto | `{a, b} = objeto` | keyword | Extraer propiedades | [ver](examples/desestructurar_objeto__destructure.js) |
| Template literal avanzado | `` `${expr}` `` | literal | Interpolación de expresiones | [ver](examples/template_expressions__backticks.js) |
| Función de orden superior | `function(fn)` | patrón | Función que recibe función | [ver](examples/funcion_orden_superior__higher_order.js) |
| Callback | `fn(callback)` | patrón | Función como argumento | [ver](examples/usar_callback__callback.js) |
| Promise básica | `new Promise()` | clase | Manejo asincrónico | [ver](examples/crear_promise__Promise.js) |
| Promise `.then()` | `promise.then()` | método | Encadenar promesas | [ver](examples/encadenar_promise__then.js) |
| Promise `.catch()` | `promise.catch()` | método | Capturar errores | [ver](examples/capturar_error__catch.js) |
| Async/await | `async / await` | keyword | Sintaxis asincrónica | [ver](examples/async_await__async.js) |
| Try/catch | `try...catch` | keyword | Manejo de excepciones | [ver](examples/capturar_error_try__try_catch.js) |
| Objeto `Math` | `Math` | objeto | Operaciones matemáticas | [ver](examples/operaciones_math__Math.js) |
| Método `Object.keys()` | `Object.keys()` | método | Obtener claves | [ver](examples/obtener_claves__Object_keys.js) |
| Método `Object.values()` | `Object.values()` | método | Obtener valores | [ver](examples/obtener_valores__Object_values.js) |
| Método `Object.entries()` | `Object.entries()` | método | Obtener pares clave-valor | [ver](examples/obtener_entradas__Object_entries.js) |
| Método `JSON.stringify()` | `JSON.stringify()` | método | Convertir a JSON | [ver](examples/convertir_json__JSON_stringify.js) |
| Método `JSON.parse()` | `JSON.parse()` | método | Parsear JSON | [ver](examples/parsear_json__JSON_parse.js) |
| Clausura (Closure) | función anidada | patrón | Mantener estado privado | [ver](examples/clausura__closure.js) |
| Operador ternario | `? :` | operador | Condicional en línea | [ver](examples/condicional_ternario__ternary.js) |
| Destructuring en parámetros | `({a, b}) => {}` | patrón | Extraer en argumentos | [ver](examples/destructuring_parametros__destructure.js) |
| Método `forEach()` | `array.forEach()` | método | Iterar con función | [ver](examples/iterar_funcion__forEach.js) |
| Método `some()` | `array.some()` | método | Verificar condición | [ver](examples/verificar_condicion__some.js) |
| Método `every()` | `array.every()` | método | Validar todos | [ver](examples/validar_todos__every.js) |

---

