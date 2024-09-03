"""
Programa que usa las clases declaradas en el archivo clases.py
Fecha 02/09/2024
Ultima modificación: 03/07/2024
"""
import clases as cl
# Crear objetos de clase Persona
per1 = cl.Persona("Juan", 70)
per2 = cl.Persona("María", 55)
# Asignar valor a las propiedades
per1.peso = 75
per2.peso = 57
per2.nombre += " Elena"
# Usar los métodos
per1.caminar()
per2.comer()
per2.comer()
print(per1)
print(per2)
per1.caminar(16)
print(per1)
per1.caminar()
print(per1)
per3 = cl.Persona()  # con la sobrecarga al constructor
print(per1)
print(per2)
print(per3)

# Crear atletas
atl1 = cl.Atleta("José", 70)
atl2 = cl.Atleta("Rosa",50)
print(atl1)
print(atl2)
# Asignar valores a la propiedad estatura
atl1.estatura = 1.65
atl2.estatura = 1.60
print('Atleta: {}, IMC={:.2f}'.format(atl1.nombre,
                                  atl1.calcular_imc()))
print('Atleta: {}, IMC={:.2f}'.format(atl2.nombre,
                                  atl2.calcular_imc()))
print(atl1)
print(atl2)
atl1 = cl.Atleta("José", 70, 1.45)
atl2 = cl.Atleta("Rosa",50, 1.8)
print('Atleta: {}, IMC={:.2f}'.format(atl1.nombre,
                                  atl1.calcular_imc()))
print('Atleta: {}, IMC={:.2f}'.format(atl2.nombre,
                                  atl2.calcular_imc()))
perX = cl.Persona("Andrea", 50)
perX.caminar()   # metodo caminar sin argumentos
print(perX)
perX.caminar(24) # metodo caminar con 1 argumento
print(perX)
perX.caminar(12, "campo") # metodo caminar con 2 argumento
print(perX)
atlX = cl.Atleta("Rodrigo", 75) # constructor con 2 argumentos
print(atlX)
print("IMC: {}".format(atlX.calcular_imc()) )
atlX.estatura = 1.73
print(atlX)
print("IMC: {:.2f}".format(atlX.calcular_imc()) )
atlY = cl.Atleta("Ximena",52, 1.60) # constructor con 3 argumentos
print(atlY)
print("IMC: {:.2f}".format(atlY.calcular_imc()) )
