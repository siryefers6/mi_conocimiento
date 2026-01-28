"""
Objetivo: Usar f-strings para interpolar valores en cadenas
Referencia: f""
Tipo: literal
Nivel: basico
"""

# f-string simple
nombre = "Ana"
print(f"Hola {nombre}")

# con expresiones
edad = 25
print(f"En 5 años tendré {edad + 5} años")

# formato de número
precio = 19.99
print(f"Precio: ${precio:.2f}")

# con variables múltiples
ciudad = "Madrid"
pais = "España"
print(f"{ciudad} está en {pais}")

"""output
Hola Ana
En 5 años tendré 30 años
Precio: $19.99
Madrid está en España
"""
