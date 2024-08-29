# Crear la Clase persona y comparar datos para 2 objetos persona
class Persona:
    # atributos o propiedades declarados
    nombre = ''
    apellido = ''
    peso = 0
    # Métodos u operaciones
    def comer(self):
        self.peso += 1
    def caminar(self):
        self.peso -= 0.5
# Realizar operaciones con clases y objetos
# Crear los objetos
per1 = Persona()
per2 = Persona()
print(per1.nombre + ', ' + per1.apellido + ', peso: ' + str(per1.peso))
# asignar valores a la propiedades
per1.nombre = 'María'
per1.apellido = 'Ramos'
per1.peso = 55

per2.nombre = 'Juan'
per2.apellido = 'Perez'
per2.peso = 70
print(per1.nombre + ', ' + per1.apellido + ', peso: ' + str(per1.peso))
# Usar los metodos de la clase
per1.comer()
per1.comer()

per2.caminar()
print(per1.nombre + ', ' + per1.apellido + ', peso: ' + str(per1.peso))
print(per2.nombre + ', ' + per2.apellido + ', peso: ' + str(per2.peso))



