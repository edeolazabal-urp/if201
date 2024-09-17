class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def calcular_bono(self):
        return self.salario * 0.1
    
    def __str__(self):
        return f'Empleado=> nombre: {self.nombre}, edad: {self.edad}, salario: {self.salario}'
    
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
    
    def calcular_bono(self):
        return self.salario * 0.2
    
    def __str__(self):
        return super().__str__() + f', departamento: {self.departamento}'