from car import Car

class   UberConfort(Car):
    aceptado    =   bool
    tapiz       =   str
    asientos    =   int
    
    def __init__(self, placa, modelo, color, anio, matricula, driver, aceptado, tapiz, asientos):
        super().__init__(placa, modelo, color, anio, matricula, driver)
        self.aceptado   =   aceptado
        self.tapiz      =   tapiz
        self.asientos   =   asientos