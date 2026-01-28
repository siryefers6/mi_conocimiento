# Python Testing - Pytest y TDD

Referencia rápida de Testing con Pytest y Test-Driven Development (TDD) en Python con ejemplos ejecutables.

---

## Conceptos Fundamentales

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Test simple | `def test_` | función | Primera prueba | [ver](examples/test_basico__primer_test.py) |
| Assert básico | `assert` | keyword | Verificar condiciones | [ver](examples/assert_basico__assert.py) |
| Assert con mensaje | `assert ... , "msg"` | keyword | Mensajes personalizados | [ver](examples/assert_mensaje__assert_msg.py) |
| Ejecutar tests | `pytest` | comando | Correr suite de tests | [ver](examples/ejecutar_tests__pytest.py) |

---

## Asserts y Validaciones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Assert igualdad | `assert a == b` | operador | Comparar valores | [ver](examples/assert_igual__eq.py) |
| Assert in | `assert x in lista` | operador | Verificar pertenencia | [ver](examples/assert_in__in.py) |
| Assert is None | `assert x is None` | operador | Verificar nulidad | [ver](examples/assert_none__is_none.py) |
| Assert is True/False | `assert bool` | operador | Verificar booleanos | [ver](examples/assert_bool__true_false.py) |
| Assert raises | `pytest.raises()` | función | Verificar excepciones | [ver](examples/assert_raises__raises.py) |
| Assert contains | `in` | operador | Verificar contenido | [ver](examples/assert_contains__contains.py) |
| Assert approx | `pytest.approx()` | función | Floats con tolerancia | [ver](examples/assert_approx__approx.py) |
| Assert con mensaje | `assert ... , "msg"` | keyword | Mensajes personalizados | [ver](examples/assert_mensaje__assert_msg.py) |
| Assert no igual | `assert a != b` | operador | Verificar diferencia | (assert_igual en negativo) |

---

## Fixtures

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Fixture básica | `@pytest.fixture` | decorador | Preparar datos para tests | [ver](examples/fixture_basica__fixture.py) |
| Fixture con scope | `scope="module"` | parámetro | Reutilizar fixtures | [ver](examples/fixture_scope__scope.py) |
| Fixture con return | `return datos` | keyword | Pasar datos a tests | [ver](examples/fixture_return__return.py) |
| Fixture con setup/teardown | `yield` | keyword | Preparar y limpiar | [ver](examples/fixture_yield__yield.py) |
| Fixture parametrizada | `params=[]` | parámetro | Multiple fixtures | [ver](examples/fixture_param__params.py) |
| Fixture request | `request.param` | parámetro | Acceder a parámetros | [ver](examples/fixture_request__request.py) |
| Fixture autouse | `autouse=True` | parámetro | Usar auto sin pedir | [ver](examples/fixture_autouse__autouse.py) |
| Fixture factory | factory function | patrón | Generar múltiples datos | [ver](examples/fixture_factory__factory.py) |

---

## Parametrización

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Parametrizar test | `@pytest.mark.parametrize` | decorador | Tests con múltiples valores | [ver](examples/parametrizar_basico__parametrize.py) |
| Parametrizar múltiple | `@pytest.mark.parametrize` doble | decorador | Dos parámetros | [ver](examples/parametrizar_doble__parametrize.py) |
| Ids personalizados | `ids=[]` | parámetro | Nombres legibles para casos | [ver](examples/parametrizar_ids__ids.py) |

---

## Excepciones y Errores

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Verificar excepción | `pytest.raises()` | función | Assert que lanza error | [ver](examples/excepcion_basica__raises.py) |
| Excepción con mensaje | `match=` | parámetro | Verificar mensaje error | [ver](examples/excepcion_mensaje__match.py) |
| Fail del test | `pytest.fail()` | función | Fallar test manualmente | [ver](examples/fail_manual__fail.py) |

---

## Markers y Opciones

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Skip test | `@pytest.mark.skip` | decorador | Saltar test | [ver](examples/marker_skip__skip.py) |
| Xfail test | `@pytest.mark.xfail` | decorador | Test esperado fallar | [ver](examples/marker_xfail__xfail.py) |
| Custom marker | `@pytest.mark.custom` | decorador | Marcador personalizado | [ver](examples/marker_custom__custom.py) |

---

## Mocking y Patches

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Mock básico | `unittest.mock.Mock` | clase | Simular objeto | [ver](examples/mock_basico__mock.py) |
| Patch de función | `@patch()` | decorador | Reemplazar función | [ver](examples/patch_funcion__patch.py) |
| Mock con return value | `return_value=` | parámetro | Valor de retorno mock | [ver](examples/mock_return__return_value.py) |

---

## TDD - Test-Driven Development

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Red-Green-Refactor | workflow | patrón | Ciclo TDD | [ver](examples/tdd_red_green__tdd.py) |
| Test primero | test first | patrón | Escribir test antes | [ver](examples/tdd_test_first__test_first.py) |
| TDD suma simple | Red → Green | patrón | Ejemplo básico TDD | [ver](examples/tdd_suma__suma.py) |
| TDD lista | Red → Green → Refactor | patrón | TDD con estructura | [ver](examples/tdd_lista__lista.py) |

---

## Organisación y Struktura

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Conftest.py | `conftest.py` | archivo | Fixtures compartidas | [ver](examples/config_conftest__conftest.py) |
| Nombres de test | `test_*.py` | convención | Nombrar archivos test | [ver](examples/estructura_nombres__test_names.py) |
| Organizar tests | `tests/` | estructura | Separar tests de código | [ver](examples/estructura_carpetas__organization.py) |

---

## Excepciones Avanzadas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Assert raises ValueError | `ValueError` | excepción | Verificar tipo error | [ver](examples/excepcion_valueerror__valueerror.py) |
| Assert raises con info | `excinfo` | variable | Acceder info excepción | [ver](examples/excepcion_info__excinfo.py) |

---

## Resumen Rápido

**Conceptos Fundamentales:** 4 ejemplos  
**Asserts:** 9 ejemplos  
**Fixtures:** 7 ejemplos  
**Parametrización:** 3 ejemplos  
**Excepciones:** 4 ejemplos  
**Markers:** 3 ejemplos  
**Mocking:** 2 ejemplos  
**Patch:** 1 ejemplo  
**TDD:** 2 ejemplos  
**Organización:** 3 ejemplos  

**Total: 38 ejemplos ejecutables**

---

## Cómo usar

1. Abre cualquier archivo `.py` en la carpeta `examples/`
2. Ejecuta: `pytest examples/nombre_archivo.py -v`
3. O ejecuta el módulo si es ejemplo standalone: `python examples/nombre_archivo.py`
4. Modifica y experimenta

Todos los ejemplos son independientes y pueden ejecutarse sin dependencias externas (solo pytest).

---

## Flujo de aprendizaje recomendado

1. **Basics** → Aprende assert y tests simples
2. **Fixtures** → Aprende a preparar datos reutilizables
3. **Parametrización** → Aprende DRY en tests
4. **Mocking** → Aisla componentes
5. **TDD** → Desarrolla guiado por tests

---

## TDD: Ciclo Red-Green-Refactor

```
RED: Escribir test que falla
  ↓
GREEN: Código mínimo para pasar test
  ↓
REFACTOR: Mejorar sin romper tests
  ↓
(repetir)
```
