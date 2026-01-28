"""
Objetivo: indice compuesto
Referencia: COMPOSITE_INDEX
Tipo: funcion
Nivel: basico
"""

-- transformacion
CREATE INDEX idx_comp ON empleados (nombre, apellido);

