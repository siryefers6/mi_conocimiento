"""
Objetivo: Usar type hints para anotaciones
Referencia: typing, ->
Tipo: módulo
Nivel: basico
"""

from typing import List, Dict, Optional

class Usuario:
    def __init__(self, nombre: str, edad: int):
        self.nombre: str = nombre
        self.edad: int = edad
    
    def obtener_info(self) -> str:
        return f"{self.nombre} ({self.edad})"
    
    def validar_edad(self) -> bool:
        return self.edad >= 18

usuario = Usuario("Ana", 30)
print(usuario.obtener_info())
print(f"Mayor de edad: {usuario.validar_edad()}")

"""output
Ana (30)
Mayor de edad: True
"""
