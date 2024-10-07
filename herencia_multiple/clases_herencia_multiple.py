'''
Herencia Múltiple: Cola, DispElectronico, DispConectividad, Teléfono
'''
from clases_lista import Cola as c, Lista as l

class DispElectronico:
    def __init__(self):
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print("El dispositivo está encendido.")
    
    def apagar(self):
        self.encendido = False
        print("El dispositivo está apagado.")

class DispConectividad:
    def __init__(self):
        self.conexion = None
    
    def conectar(self, tipo_conexion):
        if not self.conexion:
            if tipo_conexion in ["wi-fi", "plan de datos", "por cable"]:
                self.conexion = tipo_conexion
                print(f"Conectado a {tipo_conexion}.")
            else:
                print("Tipo de conexión no válido.")
        else:
            print(f"Ya estás conectado a {self.conexion}.")

    def desconectar(self):
        if self.conexion:
            print(f"Desconectado de {self.conexion}.")
            self.conexion = None
        else:
            print("No hay ninguna conexión activa.")

# Clase derivada que hereda de ambas clases
class Smartphone(DispElectronico, DispConectividad):
    def __init__(self):
        DispElectronico.__init__(self)
        DispConectividad.__init__(self)
        cola = c()
        for x in ["Video", "Juego", "Libro", "App", "Música"]:
            cola.poner(x)
        self.cola_descargas = cola
        #self.cola_descargas = c(["Video", "Juego", "Libro", "App", "Música"])

    def usar_app(self):
        if self.encendido:
            print("Usando una aplicación en el smartphone.")
        else:
            print("El teléfono está apagado. No se puede usar la aplicación.")
    
    def conectar_wifi(self, tipo_conexion):
        if self.encendido:
            self.conectar(tipo_conexion)
        else:
            print("El teléfono está apagado. No se puede conectar.")

    def descargar(self):
        if not self.encendido:
            print("El teléfono está apagado. No se puede descargar nada.")
            return
        if not self.conexion:
            print("No hay conexión. Conéctate primero.")
            return
        if self.cola_descargas:
            item = self.cola_descargas.sacar()
            print(f"Descargando {item}...")
        else:
            print("No hay más elementos para descargar.")

# Prueba la herencia múltiple
telefono = Smartphone()

# Intentar conectar cuando está apagado
telefono.conectar_wifi("wi-fi")

# Encender el teléfono
telefono.encender()

# Conectar a Wi-Fi
telefono.conectar_wifi("wi-fi")

# Descargar archivos
telefono.descargar()
telefono.descargar()

# Desconectar
telefono.desconectar()

# Intentar descargar sin conexión
telefono.descargar()

# Apagar el teléfono
telefono.apagar()

# Intentar descargar con el teléfono apagado
telefono.descargar()