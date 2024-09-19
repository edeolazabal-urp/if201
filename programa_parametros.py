'''
prueba clase Persona_parametrizada
Fecha: 05/09/2024 - TEST
'''
# del arcivo clases.py importar solo Persona_parametrizada
from clases import Persona_parametrizada as pp, Empleado as Emp
per1 = pp()
per2 = pp('Juan')
per3 = pp('Maria', 50)
print(per1)
print(per2)
print(per3)
per3.caminar(16,'campo')
print(per3)
# Prueba del ejercicio 2:
emp1 = Emp()
emp2 = Emp('Rosa')
emp3 = Emp('Pedro',22)
emp4 = Emp('Andrea', 23, 'Ingeniero')
print(emp1)
print(emp2)
print(emp3)
print(emp4)