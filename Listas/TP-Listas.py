#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas = [10, 9, 5, 7, 3, 6, 8, 4, 2, 1]
nota_alta = 0
nota_baja = 0
suma = 0
for i in range(0, 10):
  suma = suma + notas [i] 
  nota_alta =  max (notas)
  nota_baja = min (notas)
print (f"El promedio de las notas es  ", suma / 10 )
print (f"La nota más alta es {nota_alta}")
print (f"La nota más baja es {nota_baja}")

print("------------------------------***********************------------------------------------")

#2) Pedir al usuario que cargue 5 productos en una lista. • Mostrar la lista ordenada alfabéticamente. 
# Investigue el uso del método sorted ().• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range (5):
  productos.append(input("Ingrese su productos: ")) 
print(sorted(productos))
eliminar = input("Desea eliminar un producto de la lista? ")
if eliminar == productos.pop():
 print (sorted(productos))
if  (eliminar in productos):
   indice = productos.index(eliminar)
   productos.pop(indice)
   print('Listo! Hemos eliminado ', eliminar)
   print(sorted(productos))
else:
   print("El elemento NO está en la lista")

print("------------------------------***********************------------------------------------")  

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.
#pares= 0
#impares = 0

import random
lista_al_azar = [random.randint (1 , 100) for i in range (15)]

pares = [num for num in lista_al_azar if pares %2 == 0]  
impares = [num for num in lista_al_azar if impares % 2 != 0]
print("Lista completa:", lista_al_azar)
print("Números pares:", pares)
print("Números impares:", impares)

print("------------------------------***********************------------------------------------")

#4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.
datos= [1, 3, 5, 3, 7, 1, 9, 5, 3]

lista_1 = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_2 = []
for i in lista_1:
  if i not in lista_2:
    lista_2.append(i)
print (lista_1)
print (lista_2)

print("------------------------------***********************------------------------------------")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. #
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

estudiantes = ["Susana", "Federico", "Marcelo", "Dana", "Freud", "Ricardo", "Beatriz", "Tomas"]
print (estudiantes)

print("Que desea hacer?:")
print("1/Agregar estudiante")
print("2/Eliminar estudiante")

opcion = int(input())
if (opcion == 1 or opcion == 2):

 nombre = input("ingresar nombre ")
  
if opcion == 1 :
     estudiantes.append(nombre)

     if (nombre in estudiantes):
       estudiantes.pop(estudiantes.index(nombre))
     else:
        print('Estudiante no encontrado')

  
else:
  print('Opcion incorrecta')


print("------------------------------***********************------------------------------------")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el ultimo pasa a ser el primero).

lista_numeros = []

for i in range (7):
 numero = input("Ingrese un número: ")
 lista_numeros.append(numero)
 lista_invertida = lista_numeros [::-1]
print(lista_numeros)
print(lista_invertida)

print("------------------------------***********************------------------------------------")

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica

temperatura = [["15", "27" ], 
              ["10", "27" ],   
              ["20", "35" ], 
              ["20", "27" ],  
              ["9", "15" ], 
              ["14", "21" ],  
              ["30", "36" ]] 
dias_dela_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for i in range(7):
     print("El día ", dias_dela_semana[i] , " hará una temperatura de min:", temperatura[i][0], " y max de : ",temperatura[i][1])

print("------------------------------***********************------------------------------------")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia
notas = [[7, 9, 9],
         [10, 6, 8],
         [6, 7, 9],
         [9, 9, 5],
         [10, 10, 10]]
materias = ["Matematicas", "AySO", "Programacián"]

for i in range (5):    
    for i in range(len(notas)):
      print("Las notas del alumno ", i , "  son: ")      
      for j in range (3):      
        print("La nota de la materia ", materias [j], " es ", notas[i] [j] )

for i in range(5):
  suma = 0 
  for j in range(3):
    suma = suma + notas[i][j]
  print("El promedio del alumno ", i, " es ", suma/3)
  
for i in range(3):
  for j in range(5):
    suma = suma + notas[j][i]
  print("el promedio de todos los alumos es de", suma/5)

print("------------------------------***********************------------------------------------")


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 3, 2, 7, 4, 6, 8],   # Producto 1
    [1, 6, 3, 2, 5, 4, 3],   # Producto 2
    [4, 7, 8, 5, 6, 7, 2],   # Producto 3
    [2, 3, 5, 6, 4, 5, 7]    # Producto 4
]

productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 1. Total vendido por cada producto (sumar filas)
total_por_producto = []
for i in range(4):
    total = sum(ventas[i])
    total_por_producto.append(total)
    print(f"Total vendido por {productos[i]}: {total}")

print()

# 2. Día con mayores ventas totales (sumar columnas)
total_por_dia = []
for j in range(7):
    total = sum(ventas[i][j] for i in range(4))
    total_por_dia.append(total)

# Encontrar el índice del día con más ventas
indice_dia_mayor_venta = total_por_dia.index(max(total_por_dia))
print(f"El día con mayores ventas totales es {dias[indice_dia_mayor_venta]} con {total_por_dia[indice_dia_mayor_venta]} ventas.")

print()

# 3. Producto más vendido en la semana (máximo total por producto)
indice_producto_mas_vendido = total_por_producto.index(max(total_por_producto))
print(f"El producto más vendido en la semana es {productos[indice_producto_mas_vendido]} con {total_por_producto[indice_producto_mas_vendido]} unidades.")