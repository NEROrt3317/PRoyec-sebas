class Mesa:
    def __init__(self, cantidad_mesas: int) -> None:
        self.mesas = list(range(1, cantidad_mesas + 1))
    def generar_mesas(self):
        print("Mesas disponibles:", self.mesas)
    def asignar_mesa(self, num_mesa):
        if num_mesa in self.mesas:
            self.mesas.remove(num_mesa)
            print(f"La mesa {num_mesa} ha sido asignada.")
        else:
            print(f"La mesa {num_mesa} no está disponible.")
    