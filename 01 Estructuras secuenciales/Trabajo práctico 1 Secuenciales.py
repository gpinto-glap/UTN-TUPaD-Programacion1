#Punto 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!
print("Hola Mundo!")

#Punto 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando  el nombre ingresado. 

#nombre= input("ingrese un nombre")
print(f"hola{nombre}, bienvenido!")

#Punto 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
 imprima por pantalla una oración con los datos ingresados. 
nombre= input("ingrese su nombre")
apellido= input("por favor ingrese su apellido")
edad= int(input("por favor ingrese su edad actual"))
residencia= input("por favor ingrese su lugar de residencia")
print(f"soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

#Punto 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio= int(input("por favor ingrese el valor del radio para calcular el área de un círculo"))
area= 3.14*radio*radio 
perimetro= 3.14*2*radio 
print(f"el valor del área del círculo es {area} y el perímetro es {perimetro}" )

#Punto 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
segundos= int(input("Ingresar la cantidad de segundos que desea convertir en horas"))
horas= segundos/3600
print(f"{segundos} segundos equivale a {horas} horas")

#Punto 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero= int(input("por favor ingrese el número del que desea conocer su tabla de multiplicar"))
print(numero*1)
print(numero*2)
print(numero*3)
print(numero*4)
print(numero*5)
print(numero*6)
print(numero*7)
print(numero*8)
print(numero*9)
print(numero*10)

#Punto 7: Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num_1= int(input("por favor ingrese un número entero distinto de 0"))
num_2= int(input("por favor ingrese otro número entero distinto de 0"))
print(num_1 + num_2)
print(num_1 / num_2)
print(num_1 * num_2)
print(num_1 - num_2)

#punto 8:Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
altura= float(input("por favor ingrese su altura expresada en metros"))
peso= float(input("por favor ingrese su peso expresada en kilogramos"))
masa_corporal= peso/ altura**2
print(f"su masa corporal es de {masa_corporal}")

#Punto 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit
temp_Celsius= float(input("Ingrese la temperatura en grados Celsius que desea convertir en grados Fahrenheit"))
temp_Farenheit= 9/5*temp_Celsius + 32
print(f"los {temp_Celsius} grados Celsius equivalen a {temp_Farenheit} grados Fahrenheit")

#Punto 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num_1= float(input("ingrese el primer número"))
num_2= float(input("ingrese el segundo número"))
num_3= float(input("ingrese el tercer número"))
promedio= (num_1+num_2+num_3) / 3
print (f"el promedio entre los numeros {num_1}, {num_2} y {num_3} es de {promedio}")