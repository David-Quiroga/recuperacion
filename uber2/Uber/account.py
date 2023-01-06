class   Account:
    identidad   =   str
    name        =   str
    mail        =   str
    cumpleanos  =   float
    telefono    =   int
    password    =   int
    genero      =   ["Masculino","Femenino"]
    state       =   ["Quito","Rumiñahui","Mejia"]

    def __init__(self, identidad, name, mail, cumpleanos, telefono,password,genero,state):
        self.identidad  =   identidad
        self.name       =   name
        self.mail       =   mail
        self.cumpleanos =   cumpleanos
        self.telefono   =   telefono
        self.password   =   password
        self.genero     =   genero
        self.state      =   state
    
