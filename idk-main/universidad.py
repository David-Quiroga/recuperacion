from estudiante import Estudiante
from profesor   import Profesor
from rector     import Rector
from rector     import Secretaria

class Universidad:
    nombreUniversidad   = str
    secretaria          = Secretaria("", "", "", "", "", "", "")
    profesor            = Profesor("", "", "", "")
    estudiante          = Estudiante("", "", "", "", "", "")
    
    def __init__(self, nombreUniversidad, secretaria, profesor, estudiante):
        self.nombreUniversidad      = nombreUniversidad
        self.secretaria             = secretaria
        self.profesor               = profesor
        self.estudiante             = estudiante