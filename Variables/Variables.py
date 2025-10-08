##1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a 
# esta función desde el programa principal.


def imprimir_hola_mundo ():  
    print('HOla Mundo!')
    

    
imprimir_hola_mundo()

#Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el 
# programa principal solicitando el nombre al usuario.

def nombre_usuario(nombre):
    print('Hola', nombre)
    


nombre = input('Ingrese su nombre: ')
nombre_usuario(nombre)    

#CCrear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro 
# parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.


def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad}años y vivo en {residencia}')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
residencia = input('Ingrese su residencia: ')
informacion_personal(nombre, apellido, edad, residencia)

#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el
# radio al usuario y llamar ambas funciones para mostrar los resultados.

import math
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input('Ingrese el radio del circulo: '))
print(f'El área del circulo es: {calcular_area_circulo(radio)}')
print (f'El perimetro es: {calcular_perimetro_circulo(radio)}')
    



#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y 
# devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundo_a_horas(segundos):
    horas = segundos // 3600
    return horas
     
segundos = int(input('Ingrese la cantidad de segundos: '))

print('La cantidad de segundos equivalen a:', segundo_a_horas(segundos) , 'horas')

#. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva 
# su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahreheit(celsius):# (1.8 * grados c) +32
    grados = (1.8 * celsius) + 32
    return grados

grados = float(input('Ingrese los grados Celsius que sea calcular: '))
print(f'La temperatura ingresa es de: {celsius_a_fahreheit(grados)} Fahrenheit ')

#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input('Ingrese el primer número: '))
b = float(input('Ingrese el segundo número: '))
c = float(input('Ingrese el tercer número: '))

print(f'El promedio de los número ingresados es de: {calcular_promedio(a, b, c)}')


