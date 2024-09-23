'''
Gestión de listas, colas y pilas
'''
# Declaración de una lista
alumnos = []
print (alumnos)
# Agregar valores a la lista
alumnos.append('Juan')
alumnos.append('Rosa')
alumnos.append('Maria')
alumnos.append('Jose')
alumnos.append('Luis')
print (alumnos)
# mostrar los elementos en forma iterativa
for i in range(len(alumnos)):
    print(alumnos[i])

# Quitar un elemento de la lista
# sentecia del <<elem>>
# lista.pop()     # elimina el primer elemento
alumnos.pop()
print(alumnos)
alumnos.pop(2)
print(alumnos)
del alumnos[0]
print(alumnos)
# Modificar el valor de un elemento de la lista
alumnos[0] += " Maria"
print(alumnos)

# Prueba de Pila y Cola:
from clases_lista import Lista, Cola, Pila
cursos = Pila()
cursos.poner('TDS1')
cursos.poner('ADS')
cursos.poner('BD1')
cursos.poner('BD2')
print(cursos.mostrar())
cursos.sacar()
print(cursos.mostrar())
escuelas = Cola()
escuelas.poner('ingenieria')
escuelas.poner('Medicina')
escuelas.poner('Derecho')
escuelas.poner('Biologia')
print(escuelas.mostrar())
escuelas.sacar()
print(escuelas.mostrar())