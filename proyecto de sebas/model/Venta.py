#import model.Meseros as Meseros
import Meseros
class AnalizadorVentas:
    def __init__(self, cuentas=None) -> None:
        self.meseros_ventas = {}
        if cuentas is not None:
            for cuenta in cuentas:
                for pedido in cuenta.pedidos:
                    mesero = pedido['mesero']
                    total_venta = pedido['total']
                    self.agregar_venta(mesero, total_venta)
    
    def agregar_venta(self, mesero, total_venta):
        if mesero in self.meseros_ventas:
            self.meseros_ventas[mesero] += total_venta
        else:
            self.meseros_ventas[mesero] = total_venta

    def mostrar_ventas(self):
        print("Ventas por mesero:")
        for mesero, total_venta in self.meseros_ventas.items():
            print(f"{mesero}: ${total_venta}")

