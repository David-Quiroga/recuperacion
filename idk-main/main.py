from rector         import Rector
from profesor       import Profesor
from rector         import Rector
from rector         import Secretaria
from universidad    import Universidad
from estudiante     import Estudiante

if __name__ == "__main__":

    print("Rector")
    rec1    = Rector("Julio", "Agusto", "Arquitecto", 76, 98461887841)
    rec2    = Rector("Maria", "Almeda", "Magister", 54, 17816589113)
    sec1    = Secretaria("Maria", "Julieta", "Secretaria", 21, 7419878491, "Nocturna", True)
    print(vars(rec1))
    print(vars(rec2))
    print("Profesor")
    prof1   = Profesor("Antonio", "Naumane", 73, "POO")
    prof2   = Profesor("Maria", "Santander", 23, "BD")
    print(vars(prof1))
    print(vars(prof2))
    print("Estudiante")
    est1    = Estudiante("David", "Quiroga", 21, "POO", 1, "Segundo Semestre")
    est2    = Estudiante("Pedro", "Escobar", 21, "Lengua y Comunicacion", 3, "Segundo Semestre")
    print(vars(est1))
    print(vars(est2))
    print("Str")
    print(sec1)
    print("Objetos dentro de un objeto")
    uni1    = Universidad("Yavirac",sec1,prof1,est1)
    print(vars(uni1))
    print(vars(prof1))
    print(vars(est1))
    print(vars(sec1))
    uni2    = Universidad("UDLA",sec1,prof2,est2)
    print(vars(uni2))
    print(vars(prof2))
    print(vars(est2))
    print(vars(sec1))
    print("Metodo normal")
    print(est1.otroestudiante(est2))