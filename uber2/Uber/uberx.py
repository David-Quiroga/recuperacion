from car import Car

class   UberX(Car):
    def __init__(self, placa, modelo, color, anio, matricula, driver):
        super().__init__(placa, modelo, color, anio, matricula, driver)
