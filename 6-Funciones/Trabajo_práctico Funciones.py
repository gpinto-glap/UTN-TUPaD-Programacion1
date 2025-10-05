#Ejercicio 1
def imprimir_hola_mundo():
  print ("Hola Mundo")

if __name__=="__main__":
  imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
  return f"Hola {nombre}"

if __name__=="__main__":
  nombre_usuario = input("Ingrese su nombre: ")
  saludo = saludar_usuario(nombre_usuario)
  print(saludo)

#Ejercicio 3
def informacion_personal(nombre, apellido,edad, residencia):
  return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

if __name__=="__main__":
  nombre = input("Ingrese su nombre: ")
  apellido = input("Ingrese su apellido: ")
  edad = input("Ingrese su edad: ")
  residencia = input("Ingrese su residencia: ")
  informacion = informacion_personal(nombre, apellido,edad, residencia)
  print(informacion)

#Ejercicio 4
import math
def calcular_area_circulo(radio):
  area= math.pi * (radio ** 2)
  return area

def perimetro_circulo(radio):
  perimetro= 2 * math.pi * radio
  return perimetro

if __name__ == "__main__":
  radio = float(input("Ingrese el radio del circulo: "))
  area = calcular_area_circulo(radio)
  perimetro = perimetro_circulo(radio)
  print(f"El area del circulo es: {area}")
  print(f"El perimetro del circulo es: {perimetro}")

#5 Ejercicio
def segundos_a_hora(segundos):
  horas = segundos / 3600
  return horas

if __name__ == "__main__":
  segundos = float(input("Ingrese la cantidad de segundos: "))
  horas = segundos_a_hora(segundos)
  print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
def tabla_multiplicar_numero (numero):
  for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
  return resultado

if __name__ == "__main__":
  numero = int(input("Ingrese un numero: "))
  tabla_multiplicar_numero(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
  suma= a + b
  resta = a - b
  multiplicacion = a * b
  division = a / b
  return suma, resta, multiplicacion, division

if __name__ == "__main__":
  a = float(input("Ingrese el primer numero: "))
  b = float(input("Ingrese el segundo numero: "))
  suma, resta, multiplicacion, division = operaciones_basicas(a, b)
  print(f"La suma de {a} mas {b} es: {suma}")
  print(f"La resta de {a} menos {b} es: {resta}")
  print(f"La multiplicacion entre {a} y {b}: {multiplicacion}")
  print(f"La division entre {a} y {b} es: {division}")

#Ejercicio 8
def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    return imc

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"su índice de masa corporal (IM) es {imc}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
 faherenheit = (celsius * 9/5) + 32
 return faherenheit

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

#Ejercicio 10
def calcular_promedio(a, b, c):
  promedio= (a+b+c)/3
  return promedio

if __name__ == "__main__":
  a = float(input("Ingrese el primer numero: "))
  b = float(input("Ingrese el segundo numero: "))
  c = float(input("Ingrese el tercer numero: "))
  promedio = calcular_promedio(a, b, c)
  print(f"El promedio de {a}, {b} y {c} es: {promedio}")
