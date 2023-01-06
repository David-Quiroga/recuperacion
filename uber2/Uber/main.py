from    account     import  Account
from    user        import  User
from    driver      import  Driver
from    car         import  Car
from    payment     import  Payment
from    cash        import  Cash
from    route       import  Route
from    uberconfort     import  UberConfort
from    uberflash       import  UberFlash
from    uberpet         import  UberPet
from    uberx       import  UberX
from    uberxl      import  UberXL
from    trip        import  Trip

#Empieza la ejecucion
if __name__=="__main__":


    print("**OBJETOS USER**")
    usu1        = User(3131, "Julio", "eljajas@gmail.com", "01/12", "094141", "*****", "Masculino", "Mejia")
    usu2        = User(3131, "Carlos", "eljajas@gmail.com", "01/12", "094141", "*****", "Masculino", "Mejia")
    usu3        = User(3131, "Maria", "eljajas@gmail.com", "01/12", "094141", "*****", "Femenino", "Mejia")
    usu4        = User(3131, "Asher", "eljajas@gmail.com", "01/12", "094141", "*****", "Masculino", "Mejia")
    print(vars(usu1))
    print(vars(usu2))
    print(vars(usu3))
    print(vars(usu4))

    print("**OBJETOS ROUTE**")
    route1      =   Route([12,59], [32,65], 30, 10)
    route2      =   Route([41,54], [67,12], 32, 43)
    print(vars(route1))
    print(vars(route2))

    print("**OBJETOS DRIVER**")
    driver1     = Driver(46846321, "Jose", "asda@gmail.com", "12/04", "084653151", "*******", "Masculino", "Quito", "13546847687", "Nissan")
    driver2     = Driver(46846321, "Juanita", "asd548@gmail.com", "12/04", "084653151", "*******", "Femenino", "Quito", "13546847687", "Chery")
    driver3     = Driver(46846321, "Pedro", "asd548@gmail.com", "12/04", "084653151", "*******", "Masculino", "Quito", "13546847687", "Kawasaky")
    driver4     = Driver(46846321, "Maria", "asd548@gmail.com", "12/04", "084653151", "*******", "Femenino", "Quito", "13546847687", "Hiunday")
    driver5     = Driver(46846321, "Susana", "asd548@gmail.com", "12/04", "084653151", "*******", "Femenino", "Quito", "13546847687", "Mazda")
    print(vars(driver1))
    print(vars(driver2))
    print(vars(driver3))
    print(vars(driver4))
    print(vars(driver5))

    print("**OBJETOS PAYMENT**")
    payment1    =   Payment(26465, 65, usu1, driver2, "cash")
    payment2    =   Payment(534535, 12, usu1, driver2, "card")
    print(vars(payment1))
    print(vars(payment2))

    print("**OBJETOS CAR**")
    carro1      = Car("PAA-1234", "RX-8", "Verde", "2015", "889431311", driver1)
    carro2      = Car("PTO-1432", "XD-9", "Rojo", "2016", "468164818", driver1)
    print(vars(carro1))
    print(vars(carro2))    

    print("**OBJETOS UBER**")
    uberx1      =   UberX("PRR-6541", "Sentra", "Marron", "2019", "654asdsa6dd", driver1)
    uberxl1     =   UberXL("PLL-9876", "Tiggo", "Negro", "2020", "4546546asdasd", driver2, "5")
    uberflash1  =   UberFlash("PFF-1111", "Ninja", "Negro", "2009", "poqwe546468", driver3, "lentes", "5kg")
    uberpet1    =   UberPet("PPP-5521", "i10", "Blanco", "2017", "asd78d79ada", driver4, "Cerdo")
    uberconf1   =   UberConfort("PSS-6543", "RX-8", "Rojo", "2022", "984sad654as6d4ad", driver5, False, "Dorado bañado en oro", "4")
    print(vars(uberx1))
    print(vars(uberxl1))
    print(vars(uberflash1))
    print(vars(uberpet1))
    print(vars(uberconf1))

    print("**OBEJTOS TRIP**")
    trip1       =   Trip(121, usu1, driver1, route1, payment1, carro1)
    print(vars(trip1))
    print(vars(trip1.user))
    print(vars(trip1.driver))
    print(vars(trip1.route))
    print(vars(trip1.payment))
    print(vars(trip1.car))

    print("**OBJETOS TRIP 2**")    
    trip2       =   Trip(41251, usu2, driver2, route2, payment2, carro2)
    print(vars(trip1))
    print(vars(trip1.user))
    print(vars(trip1.driver))
    print(vars(trip1.route))
    print(vars(trip1.payment))
    print(vars(trip1.car))
    