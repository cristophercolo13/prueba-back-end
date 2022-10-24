from Tecnologia import Tecnologia
from Bicicleta import Bicicleta
from Consola import Consola
from Scooter import Scooter
from Tv import Tv


lista_Tv= []
lista_Consolas=[]
lista_Scooters= []
lista_Bicicleta=[] 

def registrar_Tv():
    voltage = int(input("ingrese voltage:  "))
    precio = float(input("ingrese precio:  "))
    eficiencia = input("ingrese eficiencia:  ")
    marca = input("ingrese marca:  ")
    nConsola = input("ingrese:  ")
    version = input("ingrese version:  ")
    tamaño = float(input("ingrese tamaño:  "))
    tele = Tv(voltage,precio,eficiencia,marca,nConsola,version,tamaño)
    lista_Tv.append(tele)

def registrar_Consola():
    voltage = int(input("ingrese voltage:  "))
    precio = float("ingrese precio:  ")
    eficiencia = str(input("ingrese eficiencia:  "))
    marca = input("ingrese marca:  ")
    nConsola = input("ingrese numero de consola:  ")
    version = input("ingrese version:  ")
    Consola = Consola(voltage,precio,eficiencia,marca,nConsola,version)
    lista_Consolas.append(Consola)

def registrar_Scooter():
    aro = float(input("ingrese aro:  "))
    velocidad = int(input("ingrese su velocidad: "))
    peso = float(input("ingrese peso:  "))
    voltage = int(input("ingrese voltage:  "))
    precio = float(input("ingrese precio:  "))
    eficiencia = input("ingrese eficiencia:  ")
    marca = str(input("ingrese marca:  "))
    Scooter = Scooter(aro,velocidad,peso,voltage,precio,eficiencia,marca)
    lista_Scooters.append(Scooter)

def registrar_Bicicleta():
    aro = float(input("ingrese aro:  "))
    peso = float(input("ingrese peso:  "))
    precio = float(input("ingrese precio:  "))
    marca = input("ingrese marca:  ")
    Bicicleta = Bicicleta(aro,peso,precio,marca)
    lista_Bicicleta.append(Bicicleta)

while True:
    print("1.-registrar Tv: ")
    print("2.-registrar Consola: ")
    print("3.-registrar Scooter: ")
    print("4.-registrar Bicicleta: ")
    opcion = input("Ingrese una opcion: ")
    if opcion =="1":
        registrar_Tv()
    elif opcion=="2":
        registrar_Consola()
    elif opcion=="3":
        registrar_Scooter()
    elif opcion=="4":
        registrar_Bicicleta()
    else:
        print("por favor ingrese una opcion que sea validad ")


  



