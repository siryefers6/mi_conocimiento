"""
Objetivo: Definir una clase básica
Referencia: class
Tipo: keyword
Nivel: basico
"""

# definir clase simple
class Persona:
    pass

# crear instancia
juan = Persona()
print(f"Objeto creado: {juan}")
print(f"Tipo: {type(juan)}")

# otra instancia
ana = Persona()
print(f"Objeto creado: {ana}")
print(f"¿Diferentes? {juan is not ana}")

"""output
Objeto creado: <__main__.Persona object at 0x...>
Tipo: <class '__main__.Persona'>
Objeto creado: <__main__.Persona object at 0x...>
¿Diferentes? True
"""
