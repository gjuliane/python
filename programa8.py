def run():
    limite = 1000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < limite: #Mientras potencia de dos sea menor a limite
        print("2 elevado a " + str (contador) + " es igual a: " + str(potencia_2))
        contador += 1
        potencia_2 = 2**contador

if __name__ == "__main__":
    run()


# contador = 0;
# while contador <6:
#     print("2 elevado a " + str (contador) + " es igual a: " + str(2**contador))
#     contador = contador + 1