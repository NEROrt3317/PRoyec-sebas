import random
from model import Clases
from model import Capacidad
from model import Mesas

#Capacidad
try:
    def capacidadre(self):
        for self.capacidad in Clases.Mesas:
            if Clases.Mesas.Mesa.generar_mesas>30:
                self.mesas_2=int(input("Cuantas son de dos personas: "))
                for self.mesas_2 in range(self.mesas_2):
                    self.mesas_2+=2
                self.mesas_4=int(input("Ingrese el numero de mesas de cuatro personas: "))
                for self.mesas_4 in range(self.mesas_4):
                    self.mesas_4+=4
                    return print("La cantidad de mesas de dos personas para mesas de dos es de: ",self.mesas_2),print("La cantidad de personas para mesas de cuatro es de: ",self.mesas_4)
except:
     print("Error ingrese un numero")
#Meseros
try:
     def inscribir_mesero():
        nombre = input("Ingrese el nombre del mesero: ")
        id_mesero = int(input("Ingrese el ID del mesero: "))
        clave = random.randrange(0, 11)
        return {"nombre": nombre, "id": id_mesero, "clave": clave}
except:
     print("Ingrese un nombre valido")
     print("Ingrese un id del mesro valido")