# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad_usuario:int=int(input("Por favor ingrese su edad"))
if edad_usuario>=18:
    print("usted es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota: int= int (input("por favor, ingrese la nota obtenida"))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero_par:int=int(input("Por favor ingrese un número par"))
if numero_par%2==0:
    print ("usted ha ingresado un número par")
elif numero_par!=0:
    print ("Por favor ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad_usuario:int=int(input("Por favor ingrese su edad"))
if edad_usuario<12 and edad_usuario>=0:
    print("usted es menor de edad")
elif edad_usuario>=12 and edad_usuario< 18:
    print ("usted es adolescente")
elif edad_usuario>=18 and edad_usuario<30:
    print ("usted es un joven adulto")
elif edad_usuario<0:
    print("ingrese un número positivo")
    print ("usted es un adulto") 

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

clave:str=str(input("ingresar una contraseña entre 8 y 14 caracteres"))
if len(clave) >=8 and len(clave) <=14:
   print("ha ingresado un contraseña correcta")
else: 
   print ("ha ingresado una contraseña que no cumple con lo solicitado")

#6) escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
num_aleatorio= [random.randint (1,100) for i in range (50)]
from statistics import mode, median, mean
mi_lista= (num_aleatorio)
media_calc= mean(mi_lista)
moda_calc= mode (mi_lista)
mediana_calc= median (mi_lista)
if media_calc>mediana_calc and mediana_calc>moda_calc:
    print(f"el sesgo es positivo ya que la media es de: {media_calc} y la mediana de: {mediana_calc} es mayor que la moda de: {moda_calc}")
elif media_calc<mediana_calc and mediana_calc<moda_calc:
    print (f"el sesgo es negativo ya que la media es de: {media_calc} y la mediana de: {mediana_calc} es menor que la moda de: {moda_calc}")
elif mediana_calc==mediana_calc and mediana_calc==moda_calc:
    print("sin sesgo ya que la la media, la mediana y la moda miden lo mismo")

#7)   Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
# e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla

string_ingresado:str=input("por favor ingrese una palabra")
ultimo_caracter = string_ingresado[-1].lower()
vocales= "aeiou"
if ultimo_caracter in vocales:
    print(f"{string_ingresado}!")
else:
    print (f"{string_ingresado}")

#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre_ingresado:str=input("ingrese su nombre")
num_ingresado:int=int(input("elija una opción. Si desea que su nombre se escriba en mayúscula, ingrese 1. " \
"Si desea que su nombre se escriba en minúsccula ingrese 2." \
"Si desea que su nombre se escriba solo con la primer letra en mayúscula ingrese 3"))
if num_ingresado==1:
    print(f"su nombre es {nombre_ingresado}".upper())
elif num_ingresado==2: 
    print (f"su nombre es {nombre_ingresado}".lower())
elif num_ingresado==3:
    print (f"su nombre es {nombre_ingresado}".title())

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique
#la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_sismo:float= float(input("ingrese la magnitud del sismo registrado para conocer su categoría"))
if magnitud_sismo <3:
  print("muy leve")
elif magnitud_sismo >=3 and magnitud_sismo <4:
  print ("leve")
elif magnitud_sismo >=4 and magnitud_sismo<5:
  print ("moderado")
elif magnitud_sismo >=5 and magnitud_sismo<6:
  print("fuerte")
elif magnitud_sismo >=6 and magnitud_sismo<7:
  print("muy fuerte")
elif magnitud_sismo >=7:
  print("extremo")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio:str = (input("Ingrese en que hemisferio se encuentra\n N: HEMISFERIO NORTE\n S: HEMISFERIO SUR\n")). upper()
dia = int(input("Ingrese el dia del mes\n"))
mes = int(input("Ingrese el mes del año expresado en número entero\n"))

  #HEMISFERIO NORTE:
if hemisferio == "N":
    if ((dia >= 21 and dia <=31) and (mes == 12)) or ((dia >=1 and dia<=31) and (mes >=1 and mes <=2)) or ((dia>=1 and dia <=20) and (mes == 3)):
        print ("Estas en invierno")
    elif ((dia >=21 and dia <=31) and (mes == 3)) or ((dia >= 1 and dia <=31) and (mes>= 4 and mes <=5)) or ((dia>=1 and dia<=20) and (mes== 6)):
        print ("Estas en primavera")
    elif ((dia >=21 and dia <=31) and (mes == 6)) or ((dia >= 1 and dia <=31) and (mes>= 7 and mes <=8)) or ((dia>=1 and dia<=20) and (mes== 9)):
        print ("Estas en verano")
    elif ((dia >=21 and dia <=31) and (mes == 9)) or ((dia >= 1 and dia <=31) and (mes>= 10 and mes <=11)) or ((dia>=1 and dia<=20) and (mes== 12)):
        print ("Estas en Otoño")

  #HEMISFERIO SUR:
elif hemisferio == "S":
    if ((dia >= 21 and dia <=31) and (mes == 12)) or ((dia >=1 and dia<=31) and (mes >=1 and mes <=2)) or ((dia>=1 and dia <=20) and (mes == 3)):
        print ("Estas en verano")
    elif ((dia >=21 and dia <=31) and (mes == 3)) or ((dia >= 1 and dia <=31) and (mes>= 4 and mes <=5)) or ((dia>=1 and dia<=20) and (mes== 6)):
        print ("Estas en otoño")
    elif ((dia >=21 and dia <=31) and (mes == 6)) or ((dia >= 1 and dia <=31) and (mes>= 7 and mes <=8)) or ((dia>=1 and dia<=20) and (mes== 9)):
        print ("Estas en invierno")
    elif ((dia >=21 and dia <=31) and (mes == 9)) or ((dia >= 1 and dia <=31) and (mes>= 10 and mes <=11)) or ((dia>=1 and dia<=20) and (mes== 12)):
        print ("Estas en primavera")