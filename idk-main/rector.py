class Rector:
    nombre      = str
    apellido    = str
    nivel       = str
    edad        = int
    ci          = int
    
    def __init__(self, nombre, apellido, nivel, edad, ci):
        self.nombre     = nombre
        self.apellido   = apellido
        self.nivel      = nivel
        self.edad       = edad
        self.ci         = ci 
        
class Secretaria(Rector):
    jornada         = str
    disponibilidad  = bool
    
    def __init__(self, nombre, apellido, nivel, edad, ci, jornada, disponibilidad):
        super().__init__(nombre, apellido, nivel, edad, ci)
        self.jornada        = jornada
        self.disponibilidad = disponibilidad
    
    def __str__(self):
        return f"Esta secretaria de nombre {self.nombre} {self.apellido}, tiene un nivel de {self.nivel}. Cuenta con una experiencia de {self.edad}, tambien su numero de cedula es {self.ci}"