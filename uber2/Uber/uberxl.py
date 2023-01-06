from car import Car

class   UberXL(Car):
    asientos    =   int
    def __init__(self, placa, modelo, color, anio, matricula, driver, asientos):
        super().__init__(placa, modelo, color, anio, matricula, driver)
        self.asientos   =   asientos       
