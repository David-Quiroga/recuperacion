from    user    import  User
from    driver  import  Driver
from    route   import  Route
from    payment import  Payment
from    car     import  Car

class   Trip(User, Driver, Route, Payment, Car):
    idTrip      =   int
    user		=	User("", "", "", "", "", "", "", "")
    driver		=	Driver("", "", "", "", "", "", "", "", "", "")
    route       =   Route("","","","")
    payment     =   Payment("", "", "", "", "")
    car     =   Car("", "", "", "", "", "")
    
    def __init__(self, idTrip, user, driver, route, payment, tipotrp):
        self.idTrip     =   idTrip
        self.user       =   user
        self.driver     =   driver
        self.route      =   route
        self.payment    =   payment
        self.tipotrp    =   tipotrp
        
        