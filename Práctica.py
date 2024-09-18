#1 Condicionales y Bucles (Estructuras de Control)
#Tabla de multiplicar:
#Pide al usuario un número y utiliza un bucle for para imprimir la tabla de multiplicar del 1 al 10 de ese número.
    
#n1= int(input("Ingresa el número que deseas multiplicar"))
#for i in range(1,11):
#    multiplicacion= n1*i
 #   print(multiplicacion)


#2 Números pares
#Crea un programa que le pida al usuario dos números, uno para el inicio y otro para el final de un rango.
#Utiliza un bucle for para imprimir todos los números pares dentro de ese rango.
#n1=int(input("Ingresa un primer número"))
#n2=int(input("Ingresa un segundo número"))
#for i in range(n1,n2+1):
 #   if i % 2 ==0:
  #      print(i)

#3 Promedio
#Escribe una función promedio(lista) que reciba una lista de números como parámetro y devuelva el promedio de los números.
#Crea una lista de ejemplo y pasa esa lista a la función para ver el resultado.
#numeros=[1,2,3,4,5,6,7,8,9]
#suma=sum(numeros)
#cantidad= len(numeros)
#promedio= suma/cantidad
#print(promedio)

#4 Contar vocales
#Escribe una función contar_vocales(cadena) que reciba una cadena de texto y cuente cuántas vocales tiene. Usa la función en varias cadenas de ejemplo.
#def contar_vocales(texto):
 ##  for i in (texto):
   #     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
    #        vocales= vocales+1
    #return vocales
#print(contar_vocales("melosaurio"))

#Gestión de estudiantes
#Crea un diccionario donde las claves sean los nombres de estudiantes y los valores sean sus calificaciones. Escribe funciones para:
#Añadir un nuevo estudiante.
#Eliminar a un estudiante.
#Mostrar la lista de todos los estudiantes con sus calificaciones.
estudiantes = {
    "santiago": 5,
    "mateo": 4
}
estudiantes["jose"] = 4
del (estudiantes["mateo"])
print(estudiantes)

#Análisis de ventas
#Imagina que tienes una lista con los precios de productos vendidos en un día. Escribe un programa que haga lo siguiente:

#Calcule el total de ventas del día.

#Encuentre el precio más alto y el más bajo.

#-Use un bucle for para contar cuántas ventas fueron mayores a 100 unidades monetarias.

