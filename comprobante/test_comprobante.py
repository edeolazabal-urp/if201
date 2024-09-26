'''
Pruebas unitarias de clase_comprobante
'''
import unittest
import clase_comprobante as cmp

class TestComprobante(unittest.TestCase):
    def test_caso_comprobante1_sin_importe(self):
        comp1 = cmp.Comprobante1()
        self.assertEqual(comp1.importe, 0)
        self.assertEqual(comp1.calcular_pago(), 0)

    def test_caso_comprobante2_sin_importe(self):
        comp2 = cmp.Comprobante2()
        self.assertEqual(comp2.importe, 0)
        self.assertEqual(comp2.calcular_pago(), 0)

    def test_caso_comprobante1_con_importe(self):
        comp1 = cmp.Comprobante1()
        comp1.importe = 500
        self.assertEqual(comp1.calcular_pago(), 500)
    
    def test_caso_comprobante2_con_importe(self):
        comp2 = cmp.Comprobante2(500)
        self.assertEqual(comp2.calcular_pago(), 500)

    # Pruebas de Boleta
    def test_boleta_sin_dni_sin_importe(self):
        bol = cmp.Boleta()
        self.assertEqual(bol.__str__(), 'Boleta (importe: 0, dni: )')
    
    def test_boleta_sin_dni_con_importe(self):
        bol = cmp.Boleta(500)
        self.assertEqual(bol.__str__(), 'Boleta (importe: 500, dni: )')
    
    def test_boleta_con_dni_con_importe(self):
        bol = cmp.Boleta(500, '12345678')
        self.assertEqual(bol.__str__(), 'Boleta (importe: 500, dni: 12345678)')
        self.assertEqual(bol.calcular_pago(), 500)
    
    # Pruebas de Factura
    def test_factura_sin_importe_sin_ruc(self):
        fact = cmp.Factura()
        self.assertEqual(fact.__str__(), 'Factura (importe: 0, ruc: 12345678)')
    
    def test_factura_con_importe_sin_ruc_calcular_igv(self):
        fact = cmp.Factura(500)
        self.assertEqual(fact.calcular_igv(), 90)
    
    def test_factura_con_importe_con_ruc_calcular_pago(self):
        fact = cmp.Factura(500,'1032145698')
        self.assertEqual(fact.calcular_pago(), 590)

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
