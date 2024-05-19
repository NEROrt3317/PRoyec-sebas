"""
import model.Meseros as Meseros
import model.Mesas as Mesas
import model.Venta as Venta
import model.Capacidad as Capacidad
import model.Quejas as Quejas
"""
import Meseros
import Mesas
import Venta
import Capacidad
import Quejas

#Inscripcion de mesero
inscribir_mesero = input("¿Desea inscribir a un mesero? (Si/No): ")
mesero = None
if inscribir_mesero.lower() == "si":
    mesero = Meseros.Inscripcion.inscribir_mesero()
#Asignacion de mesas 
asignar_mesas = input("¿Desea asignar mesas? (Si/No): ")
if asignar_mesas.lower() == "si":
    num_mesas = int(input("Ingrese el número de mesas del restaurante: "))
    restaurante = Mesas.Mesa(num_mesas)
    restaurante.generar_mesas()
    while True:
        num_mesa = int(input("Ingrese el número de mesa que desea asignar: "))
        restaurante.asignar_mesa(num_mesa)
        continuar = input("¿Desea asignar otra mesa? (Si/No): ")
        if continuar.lower() != "si":
            break
print("Mesero inscrito:", mesero)
#Capacidad del restaurante
print(Capacidad.CapacidadRestaurante.capacidad_total)
#Cuenta
menu = {"Perro": 10.000, "Sancocho": 15.000, "Frijoles": 15.000, "Casuela": 22.000, "Salchipapa": 12.000}
cuenta = Meseros.Cuenta(menu, Meseros.Meserosquesetienen.meseros)
analizador_ventas = Venta.AnalizadorVentas()
cuenta = Meseros.Cuenta(menu, "Nombre del mesero")
while True:
    print(menu)
    elemento_pedido = input("Ingrese qué comió el cliente (o escriba 'fin' para terminar): ")
    if elemento_pedido.lower() == "fin":
        break
    cantidad_pedida = int(input(f"Ingrese cuántas veces se pidió '{elemento_pedido}': "))
    print(Meseros.Meserosquesetienen.meseros)
    mesero = input("Ingrese el nombre del mesero que atendió: ")
    cuenta.agregar_pedido(elemento_pedido, cantidad_pedida, mesero)
    analizador_ventas.agregar_venta(mesero, menu[elemento_pedido] * cantidad_pedida)
cuenta.mostrar_cuenta()
analizador_ventas.mostrar_ventas()
#Quejas
quejas=str(input("Desea ingresar una queja(Si/No): "))
if quejas=="Si" or "si":
    Quejas.Qjas.ing_quejas()