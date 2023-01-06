from driver import Driver

class   Car:
    placa       =   str
    modelo      =   str
    color       =   str
    anio        =   str
    matricula   =   str
    driver      =   Driver("", "", "", "", "", "", "", "", "", "")
    
    def __init__(self, placa, modelo, color, anio, matricula, driver):
        self.placa      = placa
        self.modelo     = modelo
        self.color      = color
        self.anio       = anio
        self.matricula  = matricula
        self.driver     = driver
