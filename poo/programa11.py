#Busqueda lineal
#Encontrar un elemento en una lista
#Buscar en todos los elementos de manera secuencial

import random #Generar números aleatorios

def busqueda_lineal(lista, objetivo):
    match = False
    #generar un bucle
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__": #inializar el programa
    tamano_de_lista = int(input("¿De que tamaño será la lista?"))
    objetivo = int(input("¿Qué número quieres encontrar?:"))
    #Generar una lista del tamaño de la lista
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    # if encontrado:
    #     esta = "SI"
    # else:
    #     esta = "NO"
    # print(f"El elemento {objetivo} { esta } está en la lista")

    #Operador ternario
    print(f'El elemento {objetivo} { "esta" if encontrado else "no está" } en la lista')
    print(f"El elemento {objetivo} { 'esta' if encontrado else 'no está' } en la lista")
    

