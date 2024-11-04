import unittest

class Archivo:
    def __init__(self, nombre='productos.txt'):
        self.nombre = nombre

    def cargar_datos(self):
        datos = []
        with open(self.nombre, 'r') as file:
            for linea in file:
                datos.append(linea)
                # print(linea)
        return datos

    def guardar_dato(self, id, nombre, cantidad):
        with open(self.nombre, 'a') as file:
            file.write(f'{id},{nombre},{cantidad}\n')

# class producto
'''
if __name__ == '__main__':
    a = Archivo()
    # a.cargar_datos()
    a.guardar_dato(5,'Sillas',2000)
'''
class TestArchivo(unittest.TestCase):
    def test_carga_datos(self):
        a = Archivo()
        self.assertEqual(len(a.cargar_datos()), 5)

    def test_guardar_dato(self):
        a = Archivo()
        a.guardar_dato(6,'Lapiceros',3000)
        self.assertEqual(len(a.cargar_datos()), 6)        

if __name__ == '__main__':
    unittest.main()