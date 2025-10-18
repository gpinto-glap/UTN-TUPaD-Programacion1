#Ejercicio 1
precio_frutas: dict={"banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
precio_frutas["naranja"]= 1200
precio_frutas["Manzana"]= 1500
precio_frutas["Pera"]= 2300
print(precio_frutas)

#Ejercicio 2
precio_frutas["banana"]= 1330
precio_frutas["Manzana"]= 1700
precio_frutas["Melón"]= 2800
print (precio_frutas)

#Ejercicio 3
print(precio_frutas.keys())

#Ejercicio 4
contactos:dict={}

for i in range(0,4):
    contacto_ingresado= input("Por favor ingrese un nombre para su contacto: ").strip()
    
    while True:
        numero_telefonico= input ("Ahora ingrese su numero telefónico:").strip()
        if numero_telefonico.isdigit() and len(numero_telefonico)>5:
            break
        else:
            print("Por favor ingrese solo digitos (al menos 6)")
    contactos[contacto_ingresado]=numero_telefonico
print ("muchas grancias, los números fueron agendados")
contacto_buscado=input("Ingrese el nombre de la persona que desea saber su número: ").strip()
if contacto_buscado in contactos:
    numero_asociado= contactos[contacto_buscado]
    print(f"el numero telefónico del contacto {contacto_buscado} es {numero_asociado}")
else:
    print("El nombre no existe en la agenda")
print (contactos)

#Ejercicio 5
frase= input("Ingrese una frase de una oración")
frase=frase.lower()
frase= frase.split()
palabras_unicas=set(frase)
print(palabras_unicas)
frecuencia_palabras= {}
for palabras_unicas in frase:
    frecuencia_palabras[palabras_unicas]= frecuencia_palabras.get(palabras_unicas, 0) + 1
print (frecuencia_palabras)

#Ejercicio 6
def promedio_notas(notas):
  suma_notas = sum(notas)
  promedio = suma_notas / len(notas)
  return promedio

nombre1 = input("Ingrese el primer alumno: ")
notas1 = []

for i in range(3):
    nota = int(input(f"Ingrese la nota {i+1} para el alumno {nombre1}: "))
    notas1.append(nota)
tupla1 = tuple(notas1)

nombre2 = input("Ingrese el segundo alumno: ")
notas2 = []
for i in range(3):
    nota = int(input(f"Ingrese la nota {i+1} para el alumno {nombre2}: "))
    notas2.append(nota)
tupla2 = tuple(notas2)

nombre3 = input("Ingrese el tercer alumno: ")
notas3 = []

for i in range(3):
    nota = int(input(f"Ingrese la nota {i+1} para el alumno {nombre3}: "))
    notas3.append(nota)

tupla3 = tuple(notas3)

print("Los alumnos con sus notas son los siguientes: ")
print(f"alumno {nombre1}: {tupla1} alumno {nombre2}: {tupla2} alumno {nombre3}: {tupla3}")
print (f"""Los promedios de nota de cada alumno son los siguientes: 
alumno {nombre1}: promedio: {promedio_notas(tupla1)}
alumno {nombre2}: promedio: {promedio_notas(tupla2)}
alumno {nombre3}: promedio: {promedio_notas(tupla3)}""")

#Ejercicio 7
parcial1_aprobados = {"Ana", "Beto", "Carla", "Dani", "Ema"}
parcial2_aprobados = {"Carla", "Dani", "Fede", "Gaby", "Beto"}

print(f"Aprobaron Parcial 1: {parcial1_aprobados}")
print(f"Aprobaron Parcial 2: {parcial2_aprobados}\n")

ambos_aprobados = parcial1_aprobados & parcial2_aprobados
print(" Alumnos que aprobaron AMBOS parciales (Intersección):")
print(ambos_aprobados)

solo_uno_aprobado = parcial1_aprobados ^ parcial2_aprobados

print(" Alumnos que aprobaron SOLO UNO de los dos parciales (Diferencia Simétrica):")
print(solo_uno_aprobado)

total_aprobados = parcial1_aprobados | parcial2_aprobados

print(" Lista TOTAL de alumnos que aprobaron AL MENOS UN parcial (Unión):")
print(total_aprobados)

#Ejercicio 8
frutas:dict={"banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
bandera=True

while bandera:
  print("""Bienvenido al sistema de gestión de mercadería. ¿Qué desea realizar hoy?:
1- Consultar el stock de mercadería
2- Agregar unidades al stock de un producto existente
3- Agregar un nuevo producto
4- Salir""")
  opcion= input ("Elija la opción que desea realizar")
  if opcion =="1":
    print (frutas)
  
  elif opcion =="2":
    print (frutas)
    producto= input("Ingrese el nombre del producto al que desea agregar stock de unidades: ").strip().capitalize()
    if producto in frutas:
      nuevo_stock= int(input("Ingrese la cantidad de unidades a agregar: "))
      frutas[producto] += nuevo_stock
      print(f"El stock de {producto} ha sido actualizado. Nuevo stock: {frutas[producto]}")
    else: 
      print("El producto no existe en el inventario.")
    
  elif opcion =="3":
   nuevo_producto= input("Ingrese el nombre del nuevo producto: ")
   nuevo_stock= int(input("Ingrese la cantidad de unidades a agregar: "))
   frutas[nuevo_producto]= nuevo_stock
  elif opcion =="4":
    
    print("Gracias por utilizar nuestros serivios")
    bandera= False
  else:
    print("Por favor elija una opción válida. Vuelva a intentarlo")

#Ejercicio 9

agenda = {
        ("Lunes", 7): "Cierre de notas 5toE",
        ("Martes", 14): "Clase de Matemática (Repasar funciones)",
        ("Miércoles", 14): "Recuperatorio Programación 1",
        ("Jueves", 14): "Parcial 1 Organización Empresarial",
        ("Viernes", 14): "Trabajo integrador. Reunión con Maxi"
        }
print ("Agenda Semanal Guille")
print(agenda)
print ("\n")

while True:
        print("¿Qué actividad deseas consultar?")
        dia = input("Ingrese el día (Ej: Lunes, Martes): ").strip().capitalize()
        
        try:
            hora = int(input("Ingrese la hora (formato 24h, Ej: 9, 14): "))
        except ValueError:
            print("Error: La hora debe ser un número entero.")
            continue
        
        clave_consulta = (dia, hora)

        if clave_consulta in agenda:
            evento = agenda[clave_consulta]
            print(f"\n Actividad encontrada: El {dia} a las {hora}:00 tienes '{evento}'.")
        else:
            print(f"\n No hay actividad programada para el {dia} a las {hora}:00.")
            
        continuar = input("\n¿Desea hacer otra consulta? (s/n): ").strip().lower()
        if continuar != 's':
            print("Consulta finalizada.")
            break

#Ejercicio 10
paises_original = {
    "Argentina":"Buenos Aires",
    "Venezuela":"Caracas",
    "Chile":"Santiago",
    "Peru":"Lima"
}

paises_invertidos = {valor: clave for clave, valor in paises_original.items()}

print(f"Diccionario original: {paises_original}")
print(f"Diccionario invertido: {paises_invertidos}")