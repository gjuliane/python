# No repetir código

#def nombre (parametros):

def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos "+tipo_pesos+" tienes?: "))
    dolares = pesos/valor_dolar
    print("Tienes $" + str(dolares) + " dolares")

menu = """

Bienvenido al Banco Nacional de México
La siguiente aplicación te permite convertir
a dólares las siguientes monedas:

1. Pesos mexicanos
2. Pesos argentinos
3. Pesos colombianos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:   conversor("mexicanos", 20)
elif opcion == 2: conversor("argentinos", 60)
elif opcion == 3: conversor("colombianos", 120)
else: print("Ingresa una opción corecta")