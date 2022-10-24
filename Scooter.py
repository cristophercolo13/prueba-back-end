from Tecnologia import Tecnologia
from Transporte import Transporte
class Scooter(Tecnologia,Transporte):
    def __init__(self,aro:float,velocidad:int,peso:float):
        Tecnologia.__init__()
        Transporte.__init__()

        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
   
    def get__aro(self):
        return self.__aro
    def set__aro(self,aro):
        self.__aro = aro

    def get__velocidad(self):
        return self.__velocidad
    def set__velocidad(self,velocidad):
        self.__velocidad = velocidad

    def get__peso(self):
        return self.__peso
    def set__peso(self,peso):
        self.__peso  = peso
   