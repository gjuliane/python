
class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca  = marca
        self.color  = color
        self._estando = "en_reposo" #Variable privada empieza con _
        self._motor = Motor(cilindros = 4) #Variable privada empieza con _
        self._seguridad = AirBag()

    def acelerar(self, tipo):
        if tipo == "rapida":
            self._motor.inyectaGasolina(10)
            self._motor.asignarTemperatura(12)
        else:
            self._motor.inyectaGasolina(3)
            self._motor.asignarTemperatura(4)
        
        self._estando = "en movimiento"

    def desAcelerar(self, tipo):
        if tipo == "brusca":
            self._seguridad.activar()
        else:
            pass #escribir código despues

class Motor:
    def __init__(self, cilindros, tipo = "gasolina", nivelGasolina = 4600, temperatura = 0):
        self.cilindros = cilindros
        self.tipo = tipo
        self.nivelGasolina = nivelGasolina
        self.temperatura = temperatura
    
    def inyectaGasolina(self, cantidadGasolina):
        self.nivelGasolina = self.nivelGasolina - cantidadGasolina

    def asignarTemperatura(self, valor):
        self.temperatura = valor

    def informacion(self):
        print(f"nivelGasolina = {self.nivelGasolina} y temperatura = {self.temperatura}")

class AirBag:
    def __init__(self, estado = "optimo"):
        self.estado = estado

    def activar(self):
        print("Sistema de seguridad choques activados")
        self.estado = "inhabilitado"

if __name__ == "__main__":
    car1 = Automovil("2022", "Nissan - Versa", "Negro")
    car1._motor.informacion() # aquí duda propiedad privada
    car1.acelerar("lenta")
    car1._motor.informacion()
    car1.desAcelerar("brusca")