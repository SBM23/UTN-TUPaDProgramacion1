#) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos),
#  en orden creciente, mostrando un número por línea.

num_min = 0
num_max = 101

for i in range (num_min, num_max):
    print(i)


print ("---------------------------****************************-------------------------")


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingrese un número entero: ")
numero_sin_signo = numero.lstrip('-')
longitud_numero = len(numero)

if numero == numero_sin_signo:
   print (f"El número ingresado tiene {longitud_numero} digitos")
else:
      print("Debe de ingresar un numero entero")



print ("----------------------------***************************-------------------------")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario,
#  excluyendo esos dos valores.

numero1= int(input("Ingrese el primer número elegido: "))
numero2= int(input("Ingrese el segundo número elegido: "))
suma = 0

for i in range (numero1, numero2):
    if i == numero1:
        continue
     
    suma = i + suma
print("Resultado", suma)


print("----------------------------****************************-------------------------")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.


suma = 0

while i != 0 :
    i = int(input("Ingrese los numeros que desea sumar: "))
    suma = i + suma
    print (suma)
   
print("La cuenta a finalizado")

    

print("----------------------------****************************--------------------------")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el  programa debe
#  mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero = -1
intentos = 0
numero_al_azar = random.randint (0, 9)
while numero != numero_al_azar:
    numero = int(input("ingrese su intento: "))
    intentos = intentos + 1
print("La cantidad de intestos realizados es de ", intentos)
    


print("----------------------------****************************--------------------------")
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

n_min = 0
n_max = 100
for i in  range (n_max, n_min, -2):
   
    print (i)



print("----------------------------****************************--------------------------")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un  número entero positivo 
# indicado por el usuario.

count = 0
numero_usuario = int(input("Ingrese un número: "))

for i in range (0, numero_usuario):
    count += i

print(f"La suma de los numero es de {count}", )
#No se incluye el último número ingresado ya que no indica en la consigna.

print("----------------------------***************************---------------------------")

#) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos
# de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números 
# con un solo cambio).
num = 10
numeros_pares = 0
numeros_impares = 0
numero_negativos = 0
numero_positivos = 0
suma = 0
for i in range (0, num):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        numeros_pares += 1
    else:
      numeros_impares += 1
   
    if num >= 0 :
       numero_positivos += 1
    else:
       numero_negativos += 1    

print("La cantidad de numeros impares son: ", numeros_impares)
print("La cantidad de numeros pares son : ", numeros_pares)
print("La cantidad de numeros positivos son: ", numero_positivos)
print("La cantidad de numeros negativos son: ", numero_negativos)

print("----------------------------**********************---------------------------")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

numero = 3
suma = 0
for i in range (numero):
   num_media =  int(input("Ingrese un número: "))
   suma = num_media + suma
print (f"La media es de ", suma / numero)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: 
# si el usuario ingresa 547,  el programa debe mostrar 745.

numero_cadena = input("Ingrese un número: ")
numero_invertido_str = numero_cadena[::-1]
print(f"El número invertido es: {numero_invertido_str}")