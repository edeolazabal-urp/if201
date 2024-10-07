'''
Clases Lista, Pila, Cola
'''
class Lista:
    def __init__(self):
        self.elementos = []
    def sacar(self):
        pass
    def mostrar(self):
        return self.elementos
    def poner(self, dato):
        self.elementos.append(dato)
    def vacio(self):
        len(self.eleentos) == 0
    def primero(self):
        if not self.vacio():
            return self.elementos[0]
        return "la lista está vacía"
    def ultimo(self):
        if not self.vacio():
            return self.elementos[-1]  
        return "la lista está vacía"
class Pila(Lista):
    def sacar(self):
        self.elementos.pop()   # elimina el último
class Cola(Lista):
    def sacar(self):
        item = self.elementos[0]
        self.elementos.pop(0)  # elimina el primer elemento
        return item 