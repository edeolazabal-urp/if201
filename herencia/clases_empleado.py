'''
Clase empleado, nombrado, parcial
Fecha: 12/08/2024
'''
class Empleado:
    def __init__(self, nombre="sin nombre"):
        self.nombre = nombre
    def calcular(self):
        pass
    def __str__(self):
        return 'Empleado (nombre: {})'.format(self.nombre)

class Nombrado(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)  # asignar valores a la clase superior
        self.sueldo = sueldo
    def calcular(self, sueldo=None):
        if sueldo is None:
            return self.sueldo
        else:
            self.sueldo = sueldo
            return self.sueldo
    def __str__(self):
        return 'Nombrado (nombre: {}, sueldo: {})'.format(self.nombre, self.sueldo)
        
class Parcial(Empleado):
    def __init__(self, nombre, horas_trabajadas=None, tarifa_hora= None):
        super().__init__(nombre)
        if horas_trabajadas is not None:
            self.horas_trabajadas = horas_trabajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora
    def calcular(self, horas_trabajadas=None, tarifa_hora=None):
        if horas_trabajadas is not None:
            self.horas_trabajadas = horas_trabajadas
        if tarifa_hora is not None:
            self.tarifa_hora = tarifa_hora
        return self.horas_trabajadas * self.tarifa_hora
    def __str__(self):
        return 'Parcial (nombre: {}, horas_trabajadas: {}, tarifa_hora: {})'.format(self.nombre, self.horas_trabajadas, self.tarifa_hora)

 # Prueba
emp1 = Empleado()
emp2 = Empleado('Juan') 
print (emp1)
print(emp2)  
nomb1 = Nombrado('Andres',200)
nomb2 = Nombrado('Rosa', 100)
print(nomb1)
print(nomb2)
parc1 = Parcial("Maria")
parc2 = Parcial("Carlos")
parc1.horas_trabajadas = 40
parc2.horas_trabajadas = 50
parc1.tarifa_hora = 25
parc2.tarifa_hora = 24
print(parc1)
print(parc2)
print ("Para el empleado parcial: {}, el sueldo es: {}".format(parc1.nombre, parc1.calcular()))
print ("Para el empleado parcial: {}, el sueldo es: {}".format(parc2.nombre, parc2.calcular()))