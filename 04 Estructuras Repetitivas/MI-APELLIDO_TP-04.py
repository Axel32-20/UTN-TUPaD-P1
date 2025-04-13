#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

#EJERCICIO 1
for i in range(101):
    print(i)

#EJERCICIO 2
 

num = int(input("Ingrese un número entero: "))
long = len(str(num))
print(f"La cantidad de dígitos es: {long}")

#EJERCICIO 3
 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
 

for i in range(min(num1,num2) +1,max(num1,num2)):
    suma += i
print(suma)

#EJERCICIO 4
num = int(input("Ingrese un número: "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un número: "))
print(suma)

#EJERCICIO 5
import random as rd

cont = 1
num = int(input("Ingrese un número entre 0 y 9: "))
num_random = rd.randint(0,9)
while num != num_random:
    cont += 1
    num = int(input("Ingrese un número entre 0 y 9: "))

print(f"Acertaste el número en {cont} intentos")
