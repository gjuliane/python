menu = """

OPERACIONES MATEMáTICAS

1. Suma
2. Resta
3. Multiplicación
4. División
0. Salir

"""

salir = 1
while salir > 0:
    print(menu)
    opcion = int(input('Elija una opción: '))
    print("Opcion elegida: "+str(opcion))
    if opcion == 0:
        salir = 0
        print("Adios!!!")
        break

    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))

    if opcion == 1:
        print("La suma es:"+str(numero1 + numero2))

    elif opcion == 2:
        print("La resta es:"+str(numero1 - numero2))

    elif opcion == 3:
        print("La multiplicacion es:"+str(numero1 * numero2))

    elif opcion == 4:
        print("La division es:"+str(numero1 / numero2))