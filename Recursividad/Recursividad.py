#1-Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorialRecursiva(numero):
    if numero <= 2:
        return numero
    print('Calculando ', numero, ' por el factorial de ', (numero -1))
    return numero * factorialRecursiva(numero-1)
    
num = int(input('Ingrese su número: '))
print(factorialRecursiva(num))

#2-  Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def calcularFibo(pos):
    if pos<=1:
        return pos
    return calcularFibo(pos -1) + calcularFibo(pos - 2)

n = int(input('Ingrese un numero: '))
print(calcularFibo(n))

#3- Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1)
# Prueba esta función en un algoritmo general.

#Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto

def binarioRecursiva(n):
    if n <= 1:
       return str(n)

    print(f"{n} / 2 = {n // 2}  resto {n % 2}")
    # Llamada recursiva y concatenación del resto
    return binarioRecursiva(n // 2) + str(n % 2)
        
num = int(input('Ingrese el numero decimal: '))
print(f'El numero {num} es:  {binarioRecursiva(num)}') 
        
 #4- Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva 
 # True si es un palíndromo o False si no lo es.  Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().       
def es_palindromo(pal):
    lon = len(pal)
    pal = pal.lower()
    if lon <= 1:
        return True
    if lon == 2:
        return pal[0] == pal[1]
    primera = pal[0]
    ultima = pal[-1]
    nueva_palabra = pal[1:-1]
    return primera == ultima and es_palindromo (nueva_palabra)
print(es_palindromo('Neuquen'))


#5- Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
 
 #Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)
import math
def cantidad_digitos(num):
    dig = 1
    while num >= 10:
        num = num / 10
        dig = dig + 1
    return dig

def primer_num(num):
    exp = cantidad_digitos(num) -1    
    return math.trunc(num / 10** exp)

def resto_num(num):
    exp = cantidad_digitos(num) - 1
    return num - (primer_num(num) * 10**exp)

def suma_recursiva(num):
    if num <10:
        return num
        
    return primer_num(num) + suma_recursiva(resto_num(num))
    
print (suma_recursiva(876))    

   
#Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1),
# y así sucesivamente hasta llegar al último nivel con un solo bloque.

def contar_bloques(base):
    if base == 1:
        return base
    
    return base + contar_bloques(base - 1)

print( contar_bloques(5))

#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y
# un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número

def contar_digito(num, digito):
    if num <10:
        if num == digito:
            return 1
        else:
            return 0
    ultimo = num % 10
    resto = num // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
    
print(contar_digito(8456777, 7))    