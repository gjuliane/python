#Polimorfismo
#Habilidad de tomar varias formas
#En python, nos permite cambiar el comportamiento
#de una super clase, para adaptarlo a una subclase

class Persona:
#Toda clase colocar el metodo init.
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanzar(self): #No tiene parámetros
        print("Ando caminando")

class Ciclista(Persona): #La clase ciclista extiende Persona
    def __init__(self, nombre):
        super().__init__(nombre) # Inicializando super clase
    
    def avanzar(self): #Polimorfismo
        print("Ando moviendome en mi bicicleta")
    
def main():
    persona = Persona("Gustavo")
    persona.avanzar()

    ciclista = Ciclista("Gustavo fit")
    ciclista.avanzar()

if __name__ == "__main__": #Ejecutar el archivo sin inicializarlo
    main()
