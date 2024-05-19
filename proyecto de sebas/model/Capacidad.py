#import model.Mesas as Mesas
import Mesas
class CapacidadRestaurante:
    def __init__(self,capacidad,mesas_2:int,mesas_4) -> None:
        self.capacidad:int=capacidad
        self.mesas_2=mesas_2
        self.mesas_4=mesas_4
        
    def capacidadre(self):
        for self.capacidad in Mesas:
            if Mesas.Mesa.generar_mesas>30:
                self.mesas_2=int(input("Cuantas son de dos personas: "))
                for self.mesas_2 in range(self.mesas_2):
                    self.mesas_2+=2
                self.mesas_4=int(input("Ingrese el numero de mesas de cuatro personas: "))
                for self.mesas_4 in range(self.mesas_4):
                    self.mesas_4+=4
                    return print("La cantidad de mesas de dos personas para mesas de dos es de: ",self.mesas_2),print("La cantidad de personas para mesas de cuatro es de: ",self.mesas_4)
    def capacidad_total(self):
        self.capacidat= self.mesas_2 + self.mesas_4
        return print("La capacidad total es de: ",self.capacidat)
    #comentario de NRT: intento mostrar el objeto 
    def __str__(self) -> str:
        self.capacidad_total(CapacidadRestaurante)