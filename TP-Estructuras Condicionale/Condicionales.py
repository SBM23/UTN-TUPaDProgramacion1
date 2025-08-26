#) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad >= 18: 
    print ("Eres mayor de edad.")
else:
    print ("Eres menor de edad.")

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un 
# #mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Por favor ingrese la nota obtenida: "))

if nota >=6 :
    print("Aprobado.")
else:
    print("Desaprobado.")

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num1 =  int(input("Ingrese su primer número: "))


if num1  % 2 == 0:
    print("Ha ingresado un número entero")
else:
    print("Por favor, ingrese un número par")


#) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.    

edad = int(input("Ingrese su edad: "))

if edad < 12: 
    print("Eres un niño")
elif edad >= 12 and edad <18:
    print("Eres adolescente.")
elif edad >= 18 and edad <30:
    print("Eres adulto joven")
else:
   print("Eres adulto")

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
#Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una 
# #contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#  Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contrasenia = int(input("Ingrese una clave de 8 a 14 digitos que prefiera: "))
contrasenia = [1,2,3,4,5,6,7,8,9,"a","e","i","o","u"]
if len(contrasenia) >=8 and len (contrasenia) <=14:
    print(" La clave ingresada es correcta")
else:
    print("Por favor, ingrese una clave de 8 digitos")


#PUNTO 8

import random
from statistics import mode, median, mean

numero_aleatorio = [random.randint (1, 100) for i in range (50)]
print( "Lista de numero aleatorios {numero_aleatorio}")

promedio = mean(numero_aleatorio)
print(f" promedio: {promedio} ")
media = mode(numero_aleatorio)
print(f"media:{media}")
mediana = median(numero_aleatorio)
print(f"mediana: {mediana}")


#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
#  añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario,
#  dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra = input("Ingrese una palabra: ")
ultimo_caracter = palabra [-1]

vocales = "aeiouAEIOU"

if ultimo_caracter in vocales:
    print(f"La palabra es {palabra}!")
else:
    print(f"{palabra}")

# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir 
# el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python 
# para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre y luego eliga la opcion que desea ver: ")
opciones_a_elegir = int(input([" 1- Minusculas ","2- Primer letra en mayúscula","3- Mayúsculas"]))

if opciones_a_elegir == 1 :
    print("Tu nombre es" , "", nombre.lower())
elif opciones_a_elegir == 2 :
    print("Tu nombre es" , "", nombre.title())
else:
   print("Tu nombre es" , "", nombre.upper())

# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique 
# la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)


sismo = float(input("Ingrese la magnitud que desea calcular"))
if sismo < 3 :
    print ("Muy leve.")
elif sismo >= 3 and sismo < 4:
   print ("Leve")
elif sismo >=4 and sismo < 5:
    print ("Moderado")
elif sismo >=5 and sismo < 6:
    print("Fuerte", "." "Puedo causar daños a las estructuras débiles")
elif sismo >= 6 and sismo < 7:
    print("Fuerte", ".", "Puede causar daños significativos")
elif sismo >= 7 :
    print("Extremo", ".","","Causa daños a gran escala")

#Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.


mes = int(input("En que mes estas? Del 1 al 12: "))
dia = int(input("Que día es?"))
hemisferio = int(input(["Ingrese el hemisferio en el que se encuentra: " "1- Sur", "2- Norte"]))


if hemisferio == 1:
    if (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <=20):  
     print("Otoño")
    elif mes == 6 and dia<=21 or mes in [7,8]  or mes == 9 and dia <= 20:
     print("Invierno")
    elif mes == 9 and dia >= 21 or mes in [10,11] or mes == 12 and dia <=20:
     print("Primavera") 
    else:
      mes == 12 and dia >=21 or mes in [1,2] or mes == 3 and dia <=20
      print ("Verano")

if hemisferio == 2:
    if mes == 3 and dia >=21  or mes in [ 4,5 ] or mes == 6 and dia <=20:  
     print("Primavera")
    elif mes == 6 and dia <=21 or mes in [7,8] or mes == 9 and dia <= 20:
     print("Verano")
    elif mes == 9 and dia >= 21 or mes in [10,11] or mes == 12 and dia <=20:
     print("Otoño") 
    else:
      mes == 12 and dia >=21 or mes in [1,2] or mes == 3 and dia <=20
      print ("Invierno")
