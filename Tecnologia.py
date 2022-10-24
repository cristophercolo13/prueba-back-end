class Tecnologia:
    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str):
        
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
    
    def get_voltaje(self):
        return self.__voltaje
    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje
    
    def get_precio(self):
        return self.__precio
    def set_precio(self,precio):
        self.__precio = precio  

    def get_eficiencia(self):
        return self.__eficiencia
    def set_eficiencia(self,eficiencia):
        self.__eficiencia = eficiencia
    
    def get_marca(self):
        return self.__marca
    def set_marca(self,marca):
        self.__marca = marca            
