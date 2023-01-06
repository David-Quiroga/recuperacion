from car import Car

class   UberPet(Car):
    animal  =   bool
    
    def __init__(self, placa, modelo, color, anio, matricula, driver, animal):
        super().__init__(placa, modelo, color, anio, matricula, driver)
        self.animal =   animal