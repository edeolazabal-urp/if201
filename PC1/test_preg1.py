class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distancia = 0  # Inicializamos la distancia en 0 km
    
    def caminar(self):
        """Incrementa la distancia en 2 kms"""
        self.distancia += 2


class Atleta(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.calorias_consumidas = 0  # Inicializamos las calorías consumidas en 0
    
    def entrenar(self, distancia=None):
        """Entrenar:
        - Sin argumento: avanza 10 kms y consume 500 calorías por km.
        - Con argumento: avanza la distancia proporcionada y consume 500 calorías por km."""
        if distancia is None:
            distancia = 10  # Distancia predeterminada es 10 km
        self.distancia += distancia
        self.calorias_consumidas += 500 * distancia

    def competir(self, distancia=None):
        """Competir:
        - Sin argumento: avanza 20 kms y consume 750 calorías por km.
        - Con argumento: avanza la distancia proporcionada y consume 750 calorías por km."""
        if distancia is None:
            distancia = 20  # Distancia predeterminada es 20 km
        self.distancia += distancia
        self.calorias_consumidas += 750 * distancia

import unittest

class TestPersonaAtleta(unittest.TestCase):
    
    # Pruebas para la clase Persona
    def test_persona_caminar(self):
        persona = Persona("Juan")
        persona.caminar()  # Camina 2 kms
        self.assertEqual(persona.distancia, 2)  # La distancia debe ser 2 km
        persona.caminar()  # Camina otros 2 kms
        self.assertEqual(persona.distancia, 4)  # La distancia total debe ser 4 km
    
    # Pruebas para la clase Atleta
    def test_atleta_entrenar_sin_argumento(self):
        atleta = Atleta("Pedro")
        atleta.entrenar()  # Entrena 10 kms, debe consumir 500 calorías por km
        self.assertEqual(atleta.distancia, 10)
        self.assertEqual(atleta.calorias_consumidas, 5000)  # 500 cal x 10 kms

    def test_atleta_entrenar_con_argumento(self):
        atleta = Atleta("Pedro")
        atleta.entrenar(5)  # Entrena 5 kms
        self.assertEqual(atleta.distancia, 5)
        self.assertEqual(atleta.calorias_consumidas, 2500)  # 500 cal x 5 kms

    def test_atleta_competir_sin_argumento(self):
        atleta = Atleta("Pedro")
        atleta.competir()  # Compite 20 kms, debe consumir 750 calorías por km
        self.assertEqual(atleta.distancia, 20)
        self.assertEqual(atleta.calorias_consumidas, 15000)  # 750 cal x 20 kms

    def test_atleta_competir_con_argumento(self):
        atleta = Atleta("Pedro")
        atleta.competir(15)  # Compite 15 kms
        self.assertEqual(atleta.distancia, 15)
        self.assertEqual(atleta.calorias_consumidas, 11250)  # 750 cal x 15 kms

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
