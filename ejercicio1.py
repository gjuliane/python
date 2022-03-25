# Programa de descuento a través de cupones
# Aplicables en la siguiente compra
#
# En la compra de 3 productos o más se regalarán
# cupones de descuento al finalizar la compra
#
# Si compras 3 y hasta 5, se dará un cupón de 10%
# Si compras 6 y hasta 10 se aplicará un 15%
# Si comprar 11 y máximo 20 se aplicará 20%

menu = """

PROGRAMA DE LEALTAD CUPONES 2022

Reglas:

* De 3 y hasta 5
* De 6 y hasta 10
* De 11 y máximo 20

"""

print(menu)

cantidad = int(input("Ingrese la cantidad de panes comprados: "))

if cantidad > 2 and cantidad < 6:
    print("Se le ha otorgado un cupon con un 10% de descuento")
elif cantidad > 5 and cantidad < 11:
    print("Se le ha otorgado un cupon con un 15% de descuento")
elif cantidad > 10 and cantidad < 21:
    print("Se le ha otorgado un cupon con un 20% de descuento")
else:
    print("Disculpe, no se le ha otorgado ningín cupón de descuento")