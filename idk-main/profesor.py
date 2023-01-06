class Profesor:
    nombre      = str
    apellido    = str
    edad        = int
    clase       = str
    
    def __init__(self, nombre, apellido, edad, clase):
        self.nombre     = nombre    
        self.apellido   = apellido
        self.edad       = edad
        self.clase      = clase