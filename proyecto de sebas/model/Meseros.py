import random
class Inscripcion:
    def inscribir_mesero():
        nombre = input("Ingrese el nombre del mesero: ")
        id_mesero = int(input("Ingrese el ID del mesero: "))
        clave = random.randrange(0, 11)
        return {"nombre": nombre, "id": id_mesero, "clave": clave}
class Meserosquesetienen:
    meseros = [{"Juan": 516103215}, {"Carlos": 2135456654}, {"Pedro": 651564684}].append(Inscripcion.inscribir_mesero)
class Cuenta:
    def __init__(self, menu, mesero) -> None:
        self.menu = menu
        self.pedidos = []
        self.mesero = mesero
    def agregar_pedido(self, elemento, cantidad,mesero):
        self.mesero=str(input("Ingrese el nombre del mesero que atendio: "))
        if elemento in self.menu:
            total_elemento = self.menu[elemento] * cantidad
            self.pedidos.append({"elemento": elemento, "cantidad": cantidad, "total": total_elemento, "mesero": self.mesero})
        else:
            print(f"El elemento '{elemento}' no está en el menú.")
    def mostrar_cuenta(self):
        print("Cuenta:")
        for pedido in self.pedidos:
            print(f"Elemento: {pedido['elemento']}")
            print(f"Cantidad pedida: {pedido['cantidad']}")
            print(f"Total: {pedido['total']}")
            print(f"Mesero: {pedido['mesero']}")
