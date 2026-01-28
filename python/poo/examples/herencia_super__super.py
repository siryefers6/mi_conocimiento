"""
Objetivo: Usar super() para llamar métodos de la clase padre
Referencia: super()
Tipo: función
Nivel: basico
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años"

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
    
    def presentarse(self):
        padre = super().presentarse()
        return f"{padre}, matricula: {self.matricula}"

est = Estudiante("Ana", 20, "2024001")
print(est.presentarse())

"""output
Soy Ana y tengo 20 años, matricula: 2024001
"""
