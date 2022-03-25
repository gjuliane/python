Python 3.9.10 (main, Jan 17 2022, 00:00:00) 
[GCC 11.2.1 20210728 (Red Hat 11.2.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> # PROMPT colocamos nuestras instrucciones
>>> print("Hola mundo!!!")
Hola mundo!!!
>>> print("Hola mundo!!!"); print("adios mundo");"
  File "<stdin>", line 1
    print("Hola mundo!!!"); print("adios mundo");"
                                                  ^
SyntaxError: EOL while scanning string literal
>>> print("Hola mundo!!!"); print("adios mundo")
Hola mundo!!!
adios mundo
>>> 1+2
3
>>> 5-2
3
>>> #Operadores aritmeticos
>>> 5+5
10
>>> # Resta
>>> 5-3
2
>>> 10 - 9
1
>>> 20/5
4.0
>>> # Division
>>> 20/5
4.0
>>> #Division euclidiana
>>> 50000/3.5
14285.714285714286
>>> 21//5
4
>>> 50000//3.5
14285.0
>>> 21%5
1
>>> 50000%3.5
2.5
>>> # Multiplicación
>>> 5*6
30
>>> 2**2
4
>>> 5+6*3
23

>>> #importar libreria matematicas
>>> import math
>>> math.sqrt(9)
3.0
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.cos(30)
0.15425144988758405
>>> # Devuelve el valor en radianes
>>> numero = 7
>>> numero
7
>>> print(numero)
7
>>> numero1 = 3
>>> print(numero2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'numero2' is not defined
>>> print(numero1)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numero_resultado = numero + numero1
>>> numero_resultado
10
>>> # Cadena de caracteres
>>> nombre = "Gustavo"
>>> nombre
'Gustavo'
>>> apellido = "Julián"
>>> apellido
'Julián'
>>> nombre*4
'GustavoGustavoGustavoGustavo'
>>> #Numeros FLotantes
>>> numero_decimal = 3.5
>>> numero_decimal
3.5
>>> estoy_aprendiendoo = True
>>> estoy_aprendiendoo
True
>>> estoy_aprendiendoo
True
>>> edad = input("Cuántos años tienes?: ")
Cuántos años tienes?: 27
>>> edad
'27'
>>> int(edad)
27
>>> numero2 = int(input("Escribe un número"))
Escribe un número2
>>> numero2 = int(input("Escribe un número: "))
Escribe un número: 4
>>> numero2
4
>>> numero_decimal1 = 4.5
>>> numero_decimal
3.5
>>>  numero_decimal
  File "<stdin>", line 1
    numero_decimal
IndentationError: unexpected indent
>>> numero_decimal
3.5
>>> numero_decimal = 4.5
>>> numero_decimal
4.5
>>> str(numero_decimal)
'4.5'
>>> 

nombre = 'gustavo '
nombre.upper()
nombre.capitalize()
nombre.replace('g', 'G')
>>> nombre[0]
'g'
>>> nombre[0:3]
'gus'
>>> nombre[:3]
>>> nombre[::-1]
' ovatsug'
