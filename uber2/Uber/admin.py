from account import Account

class   Admin(Account):
    
    def __init__(self, identidad, name, mail, cumpleanos, telefono, password, genero, state):
        super().__init__(identidad, name, mail, cumpleanos, telefono, password, genero, state)
    
    def cancelar():
        return f'Usted ha cancelado el viaje '
