from account import Account

class   User(Account):
    
    def __init__(self, identidad, name, mail, cumpleanos, telefono, password, genero, state):
        super().__init__(identidad, name, mail, cumpleanos, telefono, password, genero, state)
    