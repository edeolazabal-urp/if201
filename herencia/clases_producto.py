'''
Herencia de producto y perecible
'''
from datetime import datetime

class Producto:
    def __init__(self, precio=None, stock=None):
        self.precio = 0.0
        self.stock = 0
        if precio:
            self.precio = precio
        if stock:
            self.stock = stock
    def inventario_valorizado(self):
        return  self.precio * self.stock

    def __str__(self):
        return f'producto (precio: {self.precio}, stock: {self.stock})'


class Perecible(Producto):
    def __init__(self, precio=None, stock=None, fecha_vencimiento='2025-09-16'):
        super().__init__(precio, stock)
        self.fecha_vencimiento = datetime.now().date()
        if fecha_vencimiento:
            self.fecha_vencimiento = datetime.strptime(fecha_vencimiento,"%Y-%m-%d").date()
        
    def sacar(self, cantidad):
        self.stock -= cantidad

    def poner(self, cantidad):
        self.stock += cantidad

    def inventario_valorizado(self):
        if self.fecha_vencimiento <  datetime.now().date():
            return 0.5 * super().inventario_valorizado()
        return super().inventario_valorizado()
    
    def __str__(self):
        return f'Perecible (precio: {self.precio}, stock: {self.stock}, fecha_vencimiento: {self.fecha_vencimiento})'

## prueba
prd1 = Producto(5,100)
print(prd1)

prd2 = Producto()
print(prd2)

prd2.precio = 4
prd2.stock = 25
print(prd2)

per1 = Perecible()
print(per1)

per1.stock = 40
per1.precio = 18
print(per1)

print(str(per1.inventario_valorizado()))

per1.fecha_vencimiento = datetime.strptime('2024-09-10',"%Y-%m-%d").date()
print(str(per1.inventario_valorizado()))
