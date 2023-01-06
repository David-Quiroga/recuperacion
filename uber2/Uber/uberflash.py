from car import Car

class   UberFlash(Car):
    encargo =   bool
    pesomax =   int
    
    def __init__(self, placa, modelo, color, anio, matricula, driver, encargo, pesomax):
        super().__init__(placa, modelo, color, anio, matricula, driver)
        self.encargo    =   encargo
        self.pesomax    =   pesomax