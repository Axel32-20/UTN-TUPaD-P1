import random as rd
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


cont = 1
num = int(input("Ingrese un número entre 0 y 9: "))
num_random = rd.randint(0,9)
while num != num_random:
    cont += 1
    num = int(input("Ingrese un número entre 0 y 9: "))

print(f"Acertaste el número en {cont} intentos")

#EJERCICIO 6 

for i in range(100 , -1 , -2):
    print(i)

#EJERCICIO 7

num = int(input("Ingrese un número entero positivo: "))

if num > 0:
    suma = 0
    for i in range(num +1 ):
        suma += i
    print(suma)

#EJERCICIO 8


num_par = 0
num_impar = 0
num_neg = 0
num_pos = 0
cont = 0 


while cont < 10 :
    num = int(input("Ingrese un número: "))
    
    if num %2 == 0:
        num_par += 1
    else:
        num_impar += 1
    if num < 0:
        num_neg += 1
    else:
        num_pos += 1
    cont += 1 
    
     
    
    
print(f"Cantidad de números pares: {num_par}")
print(f"Cantidad de números impares: {num_impar}")
print(f"Cantidad de números negativos: {num_neg}")
print(f"Cantidad de números positivos: {num_pos}")
print(f"Cantidad total de números: {cont}")

#EJERCICIO 9

cont = 0
 
while cont < 100:
    num = int(input("Ingrese un número: "))
    cont += 1

print(f"la media es {num/cont} ")

#EJERCICIO 10
num= int(input("Ingrese un número: "))
invertido = str(num)[::-1]
print(f"El número invertido es: {invertido}")



 



