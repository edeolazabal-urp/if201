'''
Gestiona productos (consulta e inserta)
Fecha: 04/11/2024
'''
from producto_data import Archivo
import tkinter as tk
from tkinter import messagebox, Entry, Label, Button, ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title = 'Gestión de Productos'
        self.archivo = Archivo()
        self.crear_controles()
        self.consultar_lista()

    def crear_controles(self):
        # Labels y Entries para los campos de datos
        self.id_entry = self.create_entry("ID:", 0)
        self.nombre_entry = self.create_entry("Nombre:", 1)
        self.cantidad_entry = self.create_entry("Cantidad:", 2)

        # Botones de la aplicación
        self.create_button("Inserta", self.insertar, 3, 0)
        self.create_button("Finalizar", self.finalizar_programa, 3, 1)

        # Tabla
        self.tabla = ttk.Treeview(self.root, columns=["Id", "Nombre", "Cantidad"], show="headings")
        #self.tabla.heading("ID", text="ID")
        #self.tabla.heading("Nombre", text="Nombre")
        #self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.grid(row=4, column=0, columnspan=2)


    def create_entry(self, text, row):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=0, padx=5, pady=5)
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    def create_button(self, text, command, row, column):
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column, padx=5, pady=5)
    
    def consultar_lista(self):
        producto = Archivo()
        productos = producto.cargar_datos()
        # limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        for registro in productos:
            self.tabla.insert('', tk.END, values=registro)

    def insertar(self):
        producto = Archivo()
        producto.guardar_dato(self.id_entry.get(), self.nombre_entry.get(), 
                          self.cantidad_entry.get())
        messagebox.showinfo("Insertar", "Producto insertado con éxito.")
        self.consultar_lista()

    def finalizar_programa(self):
        root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()