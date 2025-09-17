#Ejercicio 1
#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 
print ("------------ejercicio 1-------------")
lista_de_numeros = []
for i in range (1, 101):
    if i % 4 == 0:
        lista_de_numeros.append(i)
print (lista_de_numeros)
print()
#Ejercicio 2
#Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 
print ("------------ejercicio 2-------------")
numeros= [2,5,9,7,6]
print (f"los números de la lista son: {numeros}")
print (f"el penúltimo número es el número {numeros [-2]}")
print()
#Ejercicio 3
#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
#Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. 
print ("------------ejercicio 3-------------")
lista=[]
lista.append("arriba")
lista.append ("abajo")
lista.append ("derecha")
print (lista)
print()

#Ejercicio 4
#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,respectivamente.  
#Imprimir la lista resultante por pantalla. 
print ("------------ejercicio 4-------------")
animales = ["perro", "gato", "conejo", "pez"] 
animales[1]= "loro"
animales[3]= "oso"
print (animales)
print()
#Ejercicio 5
#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
print ("------------ejercicio 5-------------")
ejercicio_5= [8, 15, 3, 22, 7]
ejercicio_5.remove(max(ejercicio_5))
print (ejercicio_5)
print ("lo que sucede es que se elimina el número de mayor valor de la lista")
print()
#Ejercicio 6
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 
#y mostrar por pantalla los dos primeros
print ("------------ejercicio 6-------------")

ejercicio_6= [10,31,5]
print (ejercicio_6 [0:2])
print()

#Ejercicio 7
#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
print ("------------ejercicio 7-------------")
autos = ["sedan", "polo", "suran", "gol"] 
autos[1]="Jeep Renegade"
autos[2]= "Cronos"
print (autos)
print()

#Ejercicio 8
#Crear  una  lista  vacía  llamada  "dobles"  y  agregar  el  doble de 5, 10 y 15 usando append directamente. 
#Imprimir la lista resultante por pantalla. 
print ("------------ejercicio 8-------------")
dobles= []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)
print()

#Ejercicio 9
# Dada  la  lista  “compras”,  cuyos  elementos  representan  los  productos  comprados  por diferentes clientes:
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla 
print ("------------ejercicio 9-------------") 
compras  =  [["pan",  "leche"],  ["arroz",  "fideos",  "salsa"], ["agua"]] 
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print (compras)
print()

#Ejercicio 10
#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#Posición lista_anidada[0]: 15 
#  Posición lista_anidada[1]: True 
#  Posición lista_anidada[2][0]: 25.5 
#  Posición lista_anidada[2][1]: 57.9 
#  Posición lista_anidada[2][2]: 30.6 
#  Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla. 

lista_anidada= [15, True, [25.5, 57.9, 30.6], False]
print (lista_anidada)

