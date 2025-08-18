# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print ("Hola Mundo")


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo:
#    si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo 
# si utilizas print(f…) para realizar la impresión por pantalla.

nombre= input ("Ingrese su nombre")

print (f"Hola {nombre}, buenos dias")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una #
# oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# #el programa debe imprimir “Soy Marcos Pérez, tengo 30  años y vivo en Argentina”. Consejo: esto será más
#  sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Ingrese su nombre y apellido");
edad = int (input ("Ingrese su edad"));
residencia = input ("De donde eres");

print (f"Hola, soy Susa {nombre} tengo {edad} años y soy de {residencia}")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math

# Utilizare float para convertir el número entero a decimal.

radio= (float (input("Ingrese el valor: ")));

print (f"El diametro es {math.pi*radio**2:.2f}, el perimetro es {math.pi*radio*2:.2f}");

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

#entendemos que en una hora entran 3600 segundos. Esto sale de la multiplicacion entre:
# 60 segundos que equivale un minuto y 60 minutos que equivale una hora

segundos = int (input ("Ingrese los segundos que sea calcular:"))

hora= segundos//3600
print (f"Los {segundos} ingresados equivale a {hora} horas")

#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero= int(input("Ingrese la tabla que desea saber:"))


for i in range (1,11):
    resultado = numero * i 
    print (f"{numero} * {i}  {resultado}")

#7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

numero_1= int(input ("Elija un números distintos de 0:"))
numero_2 = int(input ("Ingrese el segundo números distintos de 0:"))

suma= numero_1 + numero_2
resta= numero_1 - numero_2
producto= numero_1 * numero_2
division= numero_1 / numero_2
print (f"La suma de los numeros ingresados es de: {suma}")
print (f"La resta de los numeros ingresados es de: {resta}")
print (f"La multiplicaciona de los numeros ingresados es de: {producto}")
print (f"La division de los numeros ingresados es de: {division}")

#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

grado= int(input("Ingrese la cantidad de grados Celsius que sea calcular:"))

print (f"La cantidad de Fahrenheit es de {grado * 9/5 + 32}")


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
print ("Elija tres números")
num1= (int(input("Ingresar el primer numero")))
num2= (int(input("Ingresar el segundo numero")))
num3= (int(input("Ingresar el tercer numero")))
suma = num1+num2+num3
promedio= suma // 3

print (f"El promedio de los numeros ingresados es de {promedio}")