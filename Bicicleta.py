class Bicicleta:
    def __init__(self,aro:float,precio:int,peso:float,marca:str):
        
        self.__aro = aro
        self.__precio = precio 
        self.__peso = peso
        self.__marca = marca 
   
    def get__aro(self):
        return self.__aro
    def set__aro(self,aro):
        self.__aro = aro

    def get__marca(self):
        return self.__marca
    def set__marca(self,marca):
        self.__marca = marca

    def get__precio(self):
        return self.__precio
    def set__precio(self,precio):
        self.__precio = precio

    def get__peso(self):
        return self.__peso
    def set__peso(self,peso):
        self.__peso  = peso
