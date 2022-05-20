# Complejidad algoritmica
# Nos permite comparar la eficiencia
# Entre dos algoritmos
# Predice el timepo que nos tardemos en resolver un problema
# Entender si mi algoritmo podrá resolver mi problema en el tiempo deseado

# Funcion T(n) para medir el tiempo

import time #para medir el tiempo. Importar el módulo

def factorial(n):
    respuesta = 1

    while n > 1: #Mientas n sea mayor a 1
        respuesta *= n
        n -= 1 #multiplicar por -1 la respuesta
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return
    
    return n * factorial(n -1)

if __name__ == "__main__": #Inicializar el programa
    n = 200000

    comienzo = time.time() #Ejecutar el modulo tiempo
    factorial(n)
    final = time.time() #Finalizando el módulo
    print(final - comienzo) # tiempo en segundos

    comienzo = time.time() #Ejecutar el modulo tiempo
    factorial_r(n)
    final = time.time() #Finalizando el módulo
    print(final - comienzo)  # tiempo en segundos

