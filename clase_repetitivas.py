#contador : int=0
#while contador <10 :
    
    #print(contador)
    #contador +=1

#Escribir los primero 10 número pares
#contador: int=0
#numero= 0
#while contador <10:
    #numero +=1
    #if numero%2==0:
        #print (numero)
        #contador +=1 
    

#for i in range (1, 10,3):
    #print (i)

#print (len("hola mundo")) 

#Imprimir la palabra hola mundo pero usando el bucle while

#palabra: str= "Hola mundo"
#contador : int=0
#while contador< len(palabra):
    #print (palabra [contador], end="" )
    #contador +=1


#crea un programa que imprima en pantalla todos los número enteros 
# desde 0 hasta 100 (incluyendo ambos extremos, 
# en orden creciente, mostrando un numero por línea

#Ejercicio 1
#for i in range (0,101):
    #print(i)

#i : int=0
#while i<101:
    #print (i)
    #i+=1

#Ejercicio 4. Revisar por que no ejecuta bien, no termina. Algo falta al final del código.

#numero: int=int(input("Ingrese un numero entero o 0 para terminar la ejecución"))
#suma:int=0
#while numero !=0: 
    #suma+= numero
    #numero: int= int(input("Ingrese un numero entero o 0 para terminar la ejecución"))   
    #print ("el resultado final es :" ,suma)

#Ejercicio 8: programa que permita ingresar 100 numero entero. 
# El programa debe indicar cuantos son pares, cuantos impares, cuantos negativo y cuantos positivos.
#definir canti ingresada, pares, positivos, negativos e impares. con el while ingresados <100 primero y luego 4 if,

#Desafío lúdico: desarrollar un programa que elija un número secreto y el jugador lo adivine con pistas.
#Elegir aleatoriamente entre 1 y 100 inclusive, pensar en cantidad de intentos,
#luego de cada intento si en numero ingresado es menor, mostrar más grande, si es menor, mostrar mas chico.
#al acertar mostrar acertaste en x intentos

num_ingresado: int=int(input ("ingrese un número entre 1 y 100 para adivinar el número secreto"))
contador= 1
import random
num_aleatorio= random.randint(1,101)

while num_ingresado != num_aleatorio:
    num_ingresado: int=int(input ("ingrese un número entre 1 y 100 para adivinar el número secreto"))
    contador+=1 
    if num_ingresado< num_aleatorio:
     print("elija un número más grande") 
    
    elif num_ingresado> num_aleatorio:
        print("elija un número más chico")
    else:
        print ("felicitaciones, usted a encontrado el número en:", contador, "de veces")  
    
    
#punto 2 Pensar el typing
numero=input("ingrese un numero entero: ")
if "-" in numero:
   print(len(numero)-1)
else:
   print (len(numero))

#ahora con int
numero=int (input("ingrese un numero entero: "))
cant_num= len(str(abs(numero)))
print (cant_num)

numero= input("ingrese un numero entero: ")
if not numero.isalpha():
   cant_num= len(str(abs(numero)))
   print (cant_num)
else:
   print ("ingrese un valor válido")

#con bucle
bandera: bool=True
while bandera: 
   numero= input("ingrese un numero entero: ")
   if not numero.isalpha():
      contador: int=0
      for i in numero:
        if i != "-":
            contador+=1
        print(f"la longitud del digito ingresado {numero} es {contador}")
        bandera= False
    else:
      print ("ingrese un valor válido")
      print ("--------------------------")

#10)
while bandera: 
   numero= input("ingrese un numero entero: ")
   if not numero.isalpha():
      numero_invertido=0
      numero_convertido : int=int(numero) #345
      while numero_convertido=! 0:
      digito=numero_convertido%10 #5
      numero_invertido= numero_invertido*10 + digito #5

      numero_convertido=numero_convertido//10 #34
    print (numero_invertido)
    bandera=False

    
