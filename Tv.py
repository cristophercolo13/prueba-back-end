from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self,voltage:int,precio:float,eficiencia:str,marca:str,nConsola:str,version:str,Tamaño:float):
        super().__init__(voltage,precio,eficiencia,marca)
        
        self.__Tamaño = Tamaño
    def get_Tamano(self):
        return self.__Tamaño

    def set_Tamaño(self,Tamaño):
        self.__Tamaño = Tamaño
