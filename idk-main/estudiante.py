from profesor import Profesor

class Estudiante(Profesor):
    idEstudiante    = int
    semestre        = str
    
    def __init__(self, nombre, apellido, edad, clase, idEstudiante, semestre):
        super().__init__(nombre, apellido, edad, clase)
        self.idEstudiante   = idEstudiante
        self.semestre       = semestre
    
    def otroestudiante(self, otro_estudiante):
        return f"La id de este estudiante es {self.idEstudiante}. Su nombre es {otro_estudiante.nombre}, tiene una edad de {otro_estudiante.edad}. Estudia en la clase de {self.clase} y esta en el semestre {self.semestre}"
