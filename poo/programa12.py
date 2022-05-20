#Busqueda binaria
#Hacer el programa mas pequeño
#Se llama binario porque se divide en dos
#La lista está ordenada
#Si nuestra lista está ordenada pensemos en busqueda binaria

import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f"buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}")
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2 #partir a la mitar la lista para buscar a la Izq o Der

    if lista [medio] == objetivo:
        return True
    elif lista[medio] < objetivo: 
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

if __name__ == "__main__": #inializar el programa
    tamano_de_lista = int(input("¿De que tamaño quieres la lista?"))
    objetivo = int(input("¿De número quieres encontrar?"))

    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    #[4,2,9,18]
    #[2,4,9,18]
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f"El elemento {objetivo} { 'esta' if encontrado else 'no está' } en la lista")