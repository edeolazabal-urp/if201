class Reservorio:
    def __init__(self, volumen_disponible, ubicacion):
        self.volumen_disponible = volumen_disponible  # Volumen en metros cúbicos
        self.ubicacion = ubicacion  # Ubicación del reservorio (texto)

    def llenar(self):
        """Aumenta el volumen disponible en 100 metros cúbicos."""
        self.volumen_disponible += 100


class ReservorioResidencial(Reservorio):
    def __init__(self, volumen_disponible, ubicacion, capacidad_maxima):
        super().__init__(volumen_disponible, ubicacion)
        self.capacidad_maxima = capacidad_maxima  # Capacidad máxima en metros cúbicos

    def llenar(self, volumen=None):
        """Aumenta el volumen disponible en 100 m3, pero no debe superar la capacidad máxima."""
        if volumen is None:
            volumen = 100
        if self.volumen_disponible + volumen > self.capacidad_maxima:
            self.volumen_disponible = self.capacidad_maxima
        else:
            self.volumen_disponible += volumen

    def consumir(self):
        """Resta 20 m3 al volumen disponible, pero no debe ser negativo."""
        if self.volumen_disponible - 20 < 0:
            self.volumen_disponible = 0
        else:
            self.volumen_disponible -= 20

    def calcular_consumo(self):
        """Calcula el consumo, es decir, la capacidad máxima menos el volumen disponible."""
        return self.capacidad_maxima - self.volumen_disponible


import unittest

class TestReservorio(unittest.TestCase):

    def test_reservorio_llenar(self):
        reservorio = Reservorio(200, "Lima")
        reservorio.llenar()  # Llenar 100 m3
        self.assertEqual(reservorio.volumen_disponible, 300)  # Debe ser 300 m3

    def test_reservorio_residencial_llenar_sin_superar_capacidad(self):
        reservorio_residencial = ReservorioResidencial(900, "Lima", 1000)
        reservorio_residencial.llenar()  # Llenar 100 m3
        self.assertEqual(reservorio_residencial.volumen_disponible, 1000)  # No debe superar 1000 m3

    def test_reservorio_residencial_llenar_limite(self):
        reservorio_residencial = ReservorioResidencial(950, "Lima", 1000)
        reservorio_residencial.llenar()  # Llenar 100 m3, pero no debe superar capacidad máxima
        self.assertEqual(reservorio_residencial.volumen_disponible, 1000)

    def test_reservorio_residencial_consumir(self):
        reservorio_residencial = ReservorioResidencial(50, "Lima", 1000)
        reservorio_residencial.consumir()  # Consumir 20 m3
        self.assertEqual(reservorio_residencial.volumen_disponible, 30)  # Debe ser 30 m3

    def test_reservorio_residencial_consumir_no_negativo(self):
        reservorio_residencial = ReservorioResidencial(10, "Lima", 1000)
        reservorio_residencial.consumir()  # No debe bajar de 0 m3
        self.assertEqual(reservorio_residencial.volumen_disponible, 0)  # Debe ser 0 m3

    def test_reservorio_residencial_calcular_consumo(self):
        reservorio_residencial = ReservorioResidencial(700, "Lima", 1000)
        consumo = reservorio_residencial.calcular_consumo()
        self.assertEqual(consumo, 300)  # Capacidad máxima (1000) - Volumen disponible (700)

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
