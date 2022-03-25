# Conversion de pesos mexicanos a dólares

menu = """

Bienvenido al Banco Nacional de México
La siguiente aplicación te permite convertir
a dólares las siguientes monedas:

1. Pesos mexicanos
2. Pesos argentinos
3. Pesos colombianos

Elige una opción: """

opcion = int(input(menu))


if opcion == 1:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    valor_dolar = 20
    dolares = pesos/valor_dolar
    print("Tienes " + str(dolares) + " dolares")

elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    valor_dolar = 60
    dolares = pesos/valor_dolar
    print("Tienes " + str(dolares) + " dolares")

elif opcion == 3:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    valor_dolar = 120
    dolares = pesos/valor_dolar
    print("Tienes " + str(dolares) + " dolares")

else:
    print("Ingresa una opción corecta")
