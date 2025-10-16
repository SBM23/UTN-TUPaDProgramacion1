#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas2 = {'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas.update(precios_frutas2)
print (precios_frutas)
print('---------------------********************------------------------')

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

print('---------------------********************------------------------')

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios

frutas = list(precios_frutas.keys())

for k in frutas:
    print(k)

print('---------------------********************------------------------') 

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda= {}
while True:
    print('---------------MENU DE OPCIONES---------------')
    print('1- Para agendar un nuevo contacto')
    print('2- Consultar numero de contacto')
    print('3- Salir')
    opciones= int(input('Ingrese una opcion: '))
    if opciones == 1:
        nombre = input('Por favor ingrese un nombre para poder agendarlo: ').capitalize()  
        telefono = int(input(f'Ingrese su numero de telefono {nombre}: '))
        agenda[nombre] = telefono                  
    if opciones == 2:
        consulta = input('Ingrese el contacto a consultar: ').capitalize()
        if consulta in agenda:
             print(f'El numero de {consulta} es {agenda[consulta]}')
        else:
            print('El nombre no existe en la agenda')
    if opciones == 3:
        break
print(agenda)

    
print('---------------------********************------------------------')
    
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra   
fraseUsuario = input('Ingrese una frase por favor: ')
frase = set(fraseUsuario.split())
recuento = {}
for palabra in frase:
    recuento[palabra] = frase
    
print ('Palabra unica:', palabra)
print('Palabras repetidas', recuento)

frase = input("Escribí una frase: ").lower()


palabras = frase.split()


palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras_unicas:
    recuento[palabra] = palabras.count(palabra)


print("Palabras únicas (set):")
print(palabras_unicas)

print("Cantidad de veces que aparece cada palabra:")
print(recuento)

print('---------------------********************------------------------')

#
# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumno = {}
for i in range (3):
    nombre = input(f'Ingrese el nombre del alumno {i+1}: ').capitalize()
    nota1= int(input('Ingrese la primer nota: '))
    nota2= int(input('Ingrese la segunda nota: '))
    nota3= int(input('Ingrese la tercer nota: '))
    
    notas = (nota1, nota2, nota3)
    alumno[nombre] = notas
    promedio = sum(notas) // len(notas)
   
    print(f'El promedio de {nombre} es de {promedio}')


print('---------------------********************------------------------')

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial1 = {"Ana", "Juan", "Luis", "María"}
parcial2 = {"Luis", "María", "Sofía", "Pedro"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

print('---------------------********************------------------------')


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

miDiccionario = {'Bases': 25, 'Glosh': 13, 'labiales': 20, 'rubor': 15}
opcion = 0
while True:
    print('---------------------************************-----------------------------') 
    print ('-----------MENU----------')
    print('1- Consulta de stock: ')
    print('2- agregar stock: ')
    print('3- agregar nuevo producto a catálogo: ')
    print('4- Salir')
    opcion = int(input('Ingrese la operación que desea realizar: '))

    if opcion == 1:
        producto = input('Ingrese el producto que desea consultar: ')
       
        if producto in miDiccionario:
            print(f'El stock de {producto} es de {miDiccionario[producto]}')
    if opcion == 2:
        producto = input('Ingrese el producto que desea agregar stock: ')
        if producto in miDiccionario:
            unidades = int(input('Ingrese la cantidad que desea agregar: '))
            miDiccionario[producto] = miDiccionario[producto] + unidades
        else:
            print("El producto ingresado no es valido")

    if opcion == 3:
        nuevoIngreso = input('Ingrese el producto que dese agregar al catálogo: ')
        stock = int(input('Ingrese la cantidad de stock que desea añadir: '))
        miDiccionario[nuevoIngreso] = stock
    if opcion == 4:
        break
    for key, value in miDiccionario.items():
        print(f'{key}{value}')            

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
miAgenda = {
    ('Lunes', 10): "Defensa de Tesis Doctoral",
    ('Martes', 8): 'Taller Siu',
    ('Miercoles', 14):  'Reunió Comisión Cambio Curricular',
    ('Jueves', 10): 'Comunicaciones Científicas',
    ('Viernes', 19): 'Partido Padel'
}
miAgenda[('Sabado', 10)] = 'Parcial EO'
for (dia, hora), evento in miAgenda.items():
    print(f"{dia} a las {hora}:00 : {evento}")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {
     'Argentina': 'Buenos Aires',
     'Brasil': 'Brasilia',
     'Perú': 'Lima',
     'Chile': 'Santiago',
     'Uruguay':'Montevideo',
}
capitales = {capital: pais for pais, capital in paises.items()}
print (capitales)