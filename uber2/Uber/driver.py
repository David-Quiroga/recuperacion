from account import Account

class   Driver(Account):
    licencia    =   str
    auto        =   str

    def __init__(self, identidad, name, mail, cumpleanos, telefono, password, genero, state, licencia, auto):
        super().__init__(identidad, name, mail, cumpleanos, telefono, password, genero, state)
        self.licencia   =   licencia
        self.auto       =   auto