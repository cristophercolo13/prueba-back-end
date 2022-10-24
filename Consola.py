from Tecnologia import Tecnologia
class Consola(Tecnologia):
    def __init__(self,voltage:int,precio:float,eficiencia:str,marca:str,nConsola:str,version:str):
        super().__init__(voltage,precio,eficiencia,marca)
        self.__nConsola = nConsola
        self.__version = version
       
    def get_nConsolo(self):
        return self.__nConsola
    def set_nConsola(self,nConsola):
        self.__nConsola = nConsola
    
    def get_version(self):
        return self.__version
    def set_version(self,version):
        self.__version = version  


     