import math

#coordenada tiene (x,y)
class Coordenada:
    #metodo init es un metodo especial en una clase en python
    #el objetivo es inicializar todos los atributos del objeto
    #creado, se ejecuta cuando creamos un objeto
    def __init__(self, x, y): # Se ejecuta despues de crear el objeto
        self.x = x
        self.y = y

    #formula d = raiz (x2 -x1)^2 + (y2 -y1)^2
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        return math.sqrt(x_diff + y_diff)
        # return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)
    print("El resultado de la distancia es:")
    print(coord_1.distancia(coord_2))
