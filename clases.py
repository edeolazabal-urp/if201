"""
Clases a usar en nuestros proyectos
Fecha: 02/09/2024
Ultima modificación: 03/07/2024
"""
class Persona:

    def __init__(self, *args):
        if len(args) == 0:
            self.nombre = "Sin nombre"
            self.peso = 0
        else:
            self.nombre = args[0]
            self.peso = args[1]

    def caminar(self, *args):
        if len(args) == 1:
            self.peso -= args[0] / 8.0
        elif len(args) == 2:
            if (args[1] == "campo"):
                self.peso -= args[0] / 6.0
            else:
                self.peso -= args[0] / 8.0
        else:
            self.peso -= 0.5
    def comer(self):
        self.peso +=1
    def __str__(self):
        return 'Persona (nombre={}, peso={})'.format(
            self.nombre, self.peso
        )

"""
Nueva clase: Atleta
"""    
class Atleta(Persona):
    def __init__(self, *args):
        super().__init__(args[0], args[1])  # super se refiere a la clase Persona
        if len(args) == 3:          
            self.estatura = args[2]
        else:
            self.estatura = 0.0
       

    def calcular_imc(self):  
        if self.estatura == 0:
            return 'No se puede calcular, estatura = 0'     
        return self.peso / (self.estatura * self.estatura)
    
    def __str__(self): # Permite obtener una cadena con todos los valores
        return 'Atleta (nombre={}, peso={}, estatura={})'.format(
            self.nombre, self.peso, self.estatura
        )
