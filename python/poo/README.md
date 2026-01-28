# Python POO - Guía Completa

Referencia rápida de Programación Orientada a Objetos en Python con ejemplos ejecutables.

---

## Conceptos Fundamentales

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Definir clase | `class` | keyword | Crear plantilla de objetos | [ver](examples/clase_definir__class.py) |
| Instanciar objeto | `()` | operador | Crear instancia de clase | [ver](examples/objeto_crear__instancia.py) |
| Inicializador | `__init__` | método especial | Constructor de la clase | [ver](examples/clase_init__init.py) |
| Referencia a instancia | `self` | keyword | Acceder a atributos propios | [ver](examples/instancia_self__self.py) |
| Atributo de instancia | `self.attr` | atributo | Variable de instancia | [ver](examples/atributo_instancia__self.py) |
| Atributo de clase | `class.attr` | atributo | Variable compartida | [ver](examples/atributo_clase__classvar.py) |

---

## Métodos

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Método de instancia | `def metodo(self)` | método | Función dentro de clase | [ver](examples/metodo_instancia__def.py) |
| Método de clase | `@classmethod` | decorador | Usar `cls` en lugar de `self` | [ver](examples/metodo_clase__classmethod.py) |
| Método estático | `@staticmethod` | decorador | Sin `self` ni `cls` | [ver](examples/metodo_estatico__staticmethod.py) |

---

## Propiedades y Encapsulamiento

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Atributo privado | `self._attr` | convención | Atributo de uso interno | [ver](examples/encapsulamiento_privado__underscore.py) |
| Atributo privado fuerte | `self.__attr` | convención | Name mangling | [ver](examples/encapsulamiento_fuerte__dunder.py) |
| Propiedad getter | `@property` | decorador | Acceso controlado de lectura | [ver](examples/propiedad_property__property.py) |
| Propiedad setter | `@attr.setter` | decorador | Acceso controlado de escritura | [ver](examples/propiedad_setter__setter.py) |

---

## Herencia

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Herencia simple | `class Hijo(Padre)` | estructura | Heredar de una clase | [ver](examples/herencia_basica__inherit.py) |
| Múltiple herencia | `class Hijo(Padre1, Padre2)` | estructura | Heredar de varias clases | [ver](examples/herencia_multiple__mro.py) |
| Llamar método padre | `super()` | función | Acceder a método de padre | [ver](examples/herencia_super__super.py) |
| Herencia abstracta | `ABC, @abstractmethod` | módulo/decorador | Clase base abstracta | [ver](examples/herencia_abstracta__abc.py) |

---

## Polimorfismo

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Duck typing | duck typing | patrón | Comportamiento similar sin herencia | [ver](examples/polimorfismo_duck_typing__duck.py) |
| Sobrecargar operadores | `__add__`, `__sub__`, etc | método especial | Definir comportamiento de operadores | [ver](examples/operadores_sobrecarga__operators.py) |
| Sobrecarga comparación | `__lt__`, `__gt__`, etc | método especial | Definir comparación entre objetos | [ver](examples/comparacion_sobrecarga__comparison.py) |

---

## Métodos Especiales

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Representación str | `__str__` | método especial | Conversión a string legible | [ver](examples/metodo_especial_str__str.py) |
| Representación repr | `__repr__` | método especial | Representación técnica | [ver](examples/metodo_especial_repr__repr.py) |
| Igualdad | `__eq__` | método especial | Comparación con == | [ver](examples/metodo_especial_eq__eq.py) |
| Longitud | `__len__` | método especial | Usar `len(obj)` | [ver](examples/metodo_especial_len__len.py) |
| Indexación | `__getitem__` | método especial | Acceder con `obj[índice]` | [ver](examples/metodo_especial_getitem__getitem.py) |
| Asignación índice | `__setitem__` | método especial | Asignar con `obj[índice] = valor` | [ver](examples/metodo_especial_setitem__setitem.py) |
| Iteración | `__iter__` | método especial | Hacer objeto iterable | [ver](examples/metodo_especial_iter__iter.py) |
| Llamada | `__call__` | método especial | Invocar objeto como función | [ver](examples/metodo_especial_call__call.py) |
| Context manager | `__enter__, __exit__` | método especial | Usar con statement | [ver](examples/metodo_especial_enter_exit__context.py) |

---

## Composición y Agregación

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Composición | composición | patrón | Objetos contienen otros objetos | [ver](examples/composicion__composition.py) |

---

## Estructuras de Datos Personalizadas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Generador en clase | `yield` | método especial | Iterar con yield | [ver](examples/generador_clase__generator.py) |

---

## Patrones y Buenas Prácticas

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Excepciones personalizadas | `class Error(Exception)` | clase | Crear excepciones propias | [ver](examples/excepcion_personalizada__custom.py) |
| Singleton | Singleton | patrón | Una sola instancia de la clase | [ver](examples/singleton_patron__singleton.py) |
| Factory | Factory | patrón | Crear objetos sin especificar clase exacta | [ver](examples/factory_patron__factory.py) |
| Decorador propio | `@decorator` | decorador | Crear decorador personalizado | [ver](examples/decorador_propio__decorator.py) |

---

## Dataclasses y Type Hints

| Concepto | Referencia | Tipo | Uso | Ejemplo |
|----------|-----------|------|-----|---------|
| Dataclass básica | `@dataclass` | decorador | Simplificar clases con datos | [ver](examples/dataclass_basica__dataclass.py) |
| Post-init en dataclass | `__post_init__` | método especial | Inicialización adicional en dataclass | [ver](examples/dataclass_postinit__post_init.py) |
| Type hints | `typing` | módulo | Anotación de tipos | [ver](examples/typing_hints__typing.py) |
| Metaclase | `metaclass` | patrón avanzado | Controlar creación de clases | [ver](examples/metaclass_basica__metaclass.py) |

---

## Resumen Rápido

**Conceptos fundamentales:** 6 ejemplos  
**Métodos:** 3 ejemplos  
**Propiedades:** 4 ejemplos  
**Herencia:** 4 ejemplos  
**Polimorfismo:** 3 ejemplos  
**Métodos especiales:** 9 ejemplos  
**Composición:** 1 ejemplo  
**Estructuras de datos:** 1 ejemplo  
**Patrones:** 4 ejemplos  
**Dataclasses:** 4 ejemplos  

**Total: 39 ejemplos ejecutables**

---

## Cómo usar

1. Abre cualquier archivo `.py` en la carpeta `examples/`
2. Ejecuta el script: `python examples/nombre_archivo.py`
3. Observa el output en la sección `"""output`
4. Modifica el código para experimentar

Todos los ejemplos son independientes y pueden ejecutarse sin dependencias externas.
