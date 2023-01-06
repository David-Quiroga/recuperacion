from  payment import Payment

class   Card(Payment):
    tipo_trg        =   str
    id_card         =   int
    cod_seguridad   =   int
    
    def __init__(self, ide, ammount, user, driver, tipo, tipo_trg, id_card, cod_seguridad):
        super().__init__(ide, ammount,user,driver,tipo)
        self.tipo_trg       =   tipo_trg
        self.id_card        =   id_card
        self.cod_seguridad  =   cod_seguridad