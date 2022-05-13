class Lavadora: #crear una clase
    def __init__(self): #crear un constructor
        pass

    def lavar(self, temperatura = "caliente"):
        # llamar varios métodos
        self._llevar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llevar_tanque_de_agua(self, temperatura): #definir el llenado
        # self.temperatura = temperatura
        print(f"Llenando el tanque de agua {temperatura}") #interpolación
    
    def _anadir_jabon(self):
        print("Añadiendo jabón")

    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("Centrifugando la ropa")


#punto de entrada de la aplicación
#este archivo se ejecuta en este momento
if __name__ == "__main__":
    lavadora = Lavadora()
    # print(lavadora)
    lavadora.lavar()
    lavadora.lavar("fria")
