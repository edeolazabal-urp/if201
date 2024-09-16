import unittest
from prueba.clases_producto import Perecible, Producto

class TestPrograma(unittest.TestCase):
    # Métodos de Prueba
    def test_producto_sin_argumentos(self):
        prd1 = Producto()
        self.assertEqual(prd1.inventario_valorizado(), 0)

    def test_perecible_vigente(self):
       per1 = Perecible(5, 150, '2024-12-01')
       self.assertEqual(per1.inventario_valorizado(), (5*150))

    def test_perecible_vencido(self):
       per1 = Perecible(5, 150, '2024-09-01')
       self.assertEqual(per1.inventario_valorizado(), (5*150/2))

if __name__ == '__main__':
 unittest.main()