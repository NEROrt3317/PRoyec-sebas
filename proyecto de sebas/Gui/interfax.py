import tkinter as tk
from tkinter import messagebox

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante")
        
        # Título
        title_label = tk.Label(root, text="Bienvenido al Restaurante", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Menú
        self.menu = {
            "Hamburguesa": 5.50,
            "Pizza": 8.00,
            "Ensalada": 4.00,
            "Soda": 1.50,
            "Agua": 1.00
        }
        
        # Crear variables para cada ítem del menú
        self.orders = {}
        for item in self.menu:
            self.orders[item] = tk.IntVar()

        # Crear los checkbuttons y las entradas para la cantidad
        row = 1
        for item, price in self.menu.items():
            checkbutton = tk.Checkbutton(root, text=f"{item} - ${price:.2f}", variable=self.orders[item])
            checkbutton.grid(row=row, column=0, sticky="w")
            
            quantity_entry = tk.Entry(root)
            quantity_entry.grid(row=row, column=1)
            self.orders[item].entry = quantity_entry
            
            row += 1
        
        # Botón para calcular total
        calc_button = tk.Button(root, text="Calcular Total", command=self.calcular_total)
        calc_button.grid(row=row, column=0, columnspan=2, pady=10)
        
        # Etiqueta para mostrar el total
        self.total_label = tk.Label(root, text="Total: $0.00", font=("Helvetica", 14))
        self.total_label.grid(row=row+1, column=0, columnspan=2, pady=5)
    
    def calcular_total(self):
        total = 0.0
        for item, var in self.orders.items():
            if var.get():
                quantity_str = var.entry.get()
                if quantity_str.isdigit():
                    quantity = int(quantity_str)
                    total += self.menu[item] * quantity
                else:
                    messagebox.showerror("Entrada inválida", f"Por favor, ingrese una cantidad válida para {item}")
                    return
        
        self.total_label.config(text=f"Total: ${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()
