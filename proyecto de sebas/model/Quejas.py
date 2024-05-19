#import model.Mesas as Mesas
import Mesas
class Qjas:
    def __init__(self,quejas:str,queja:str,queja_mesa) -> None:
        self.quejas=quejas
        self.queja=queja
        self.queja_mesa=queja_mesa
    def ing_quejas(self):
        for self.quejas in Mesas:
            if self.quejas == "Si" or "si":
                self.queja=str(input("Ingrese la queja: "))
                self.queja_mesa=int(input("Ingrese la mesa que se quejo"))
                return self.queja,self.queja_mesa
            