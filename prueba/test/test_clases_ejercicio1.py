import unittest
from prueba.clases_empleado import Empleado, Gerente

class TestEmpleado(unittest.TestCase):
    def test_propiedades_empleado(self):
        emp1 = Empleado('Juan',20, 2000)
        self.assertEqual(emp1.__str__(), 'Empleado=> nombre: Juan, edad: 20, salario: 2000')
    
    def test_bono_empleado(self):
        emp = Empleado ('Maria',25,2000)
        self.assertEqual(emp.calcular_bono(),200)

    def test_propiedades_gerente(self):
        ger = Gerente('Pedro',35, 5000, 'Ventas')
        self.assertEqual(ger.__str__(), 'Empleado=> nombre: Pedro, edad: 35, salario: 5000, departamento: Ventas')

    def test_bono_gerente(self):
        ger = Gerente('Pedro',35, 5000, 'Ventas')
        self.assertEqual(ger.calcular_bono(), 1000)

if __name__ == '__main__':
 unittest.main()