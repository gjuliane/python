def run():
    texto = input("Escribe una palabra")
    for letra in texto:
        if letra == 'o': break
        print(letra)

if __name__ == "__main__":
    run()


# contador = 0;
# while contador <6:
#     print("2 elevado a " + str (contador) + " es igual a: " + str(2**contador))
#     contador = contador + 1