#Una clase tiene:
#Estado, propiedades, comportamiento

#Crear una clase para contruir coches

class Coche():
    largochasis = 250 #Primera propiedad
    anchochasis = 120 #Segunda propiedad
    rueda = 4
    enmarcha = False

    #Un objeto tiene un cmoportamiento
    #crear métodos

    #(parameter) self: Self@Coche
    def arrancar (self): #Crear un método, self hace referencia al propio objeto de la clase
        self.enmarcha = True

    def estado (self):
        if (self.enmarcha):
            return "El coche está en marcha"

        else:
            return "El coche está parado"

miCoche = Coche() #Crear mi primer objeto. Instanciar una clase
print("El largo de mi coche es:", miCoche.largochasis)
print("El coche tiene", miCoche.rueda, "ruedas")
miCoche.arrancar
print(miCoche.estado())