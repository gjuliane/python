# El programa te permite convertir los
# pesos mexicanos a dolares

pesos = input("Cuántos pesos mexicanos deseas convertir a dólares?: ")
pesos = float(pesos)

valor_dolar = 20;

dolares = pesos/valor_dolar

print("Tienes $" + str(dolares) + " dólares")
