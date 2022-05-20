import random

def ordenamiento_de_burbuja(lista):
    n = len(lista) #LONGITUD DE LA LISTA
    for i in range(n): #n tamaño de la lista
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
            if lista[j] > lista[j + 1]:#intercambiando los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

#[8,6,3,2]
#[6,8,3,2]
#[6,3,8,2]