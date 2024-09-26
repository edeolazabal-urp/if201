'''
Ejemplo de Herencia: Comprobante, Factura, Boleta
'''
class Comprobante1:
    importe=0
    def calcular_pago(self):
        return self.importe

class Comprobante2:
    def __init__(self, importe=0):
        self.importe = importe
    def calcular_pago(self):
        return self.importe
    
# Clase que heredan
class Boleta(Comprobante2):
    def __init__(self, importe=0, dni=None):
        super().__init__(importe)
        self.dni=""
        if dni is not None:
            self.dni = dni
    def __str__(self):
        return f'Boleta (importe: {self.importe}, dni: {self.dni})'

class Factura(Comprobante2):
    def __init__(self, importe=0, ruc='12345678'):
        super().__init__(importe)
        self.ruc = ruc
    def calcular_igv(self):
        return 0.18 * self.importe
    def calcular_pago(self):
        # Si el importe es mayor a 250 soles entonces se aplica un descuento de 5% al total de pago (con igv incluido)
        if self.importe > 250:
            return (1 - 0.05) * (super().calcular_pago() + self.calcular_igv())
        return super().calcular_pago() + self.calcular_igv()
    def __str__(self):
        return f'Factura (importe: {self.importe}, ruc: {self.ruc})'

# Prueba
fact = Factura(251,'98765432')
# print('importe: ' + str(fact.importe) + ', ruc: ' + fact.ruc)
print(fact.calcular_pago())