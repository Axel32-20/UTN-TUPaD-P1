from statistics import mode,median,mean
import random as rd

#3 ESTRUCTURAS CONDICIONALES - PRÁCTICO 3 - AXEL LE ROUX  

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

def mayor_de_edad(edad):
    if edad > 18:
        return "Es mayor de edad"
    else:
        return "No es mayor de edad"


edad_persona = int(input("Ingrese su edad: "))
resultado = mayor_de_edad(edad_persona)
print(resultado)

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

def estado_nota(nota):
    if nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

nota_persona = int(input("Ingrese su nota: "))
resultado_nota = estado_nota(nota_persona)
print(resultado_nota)

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

def es_par(num):
    if num %2 == 0:
        return "Ha ingresado un número par"
    else:
        return "Por favor, ingrese un número par"
    
num_persona = int(input("Ingrese un número: "))
resultado_par = es_par(num_persona)
print(resultado_par)

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

def cat_edad(edad):
    if edad < 12:
        return "Niño/a"
    elif edad >= 12 and edad < 18:
        return "Adolescente"
    elif edad >= 18 and edad < 30:
        return "Adulto/a joven"
    else:
        return "Adulto/a"

edad_persona = int(input("Ingrese su edad: "))
resultado_Edad = cat_edad(edad_persona)
print(resultado_Edad)

# 5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres

def contraseña (num):
    if len(num) >= 8 and len(num) :
        return "Ha ingresado una contraseña correcta"
    else:
        return "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

contraseña_persona = input("Ingrese su contraseña: ")
resultado_contraseña = contraseña(contraseña_persona)
print(resultado_contraseña)

#6 
def det_sesgo(moda,mediana,media):
    if media > mediana and mediana > moda :
        return "Sesgo positivo o a la derecha"
    elif media < mediana and mediana < moda:
        return "Sesgo negativo o a la izquierda"
    else:
        return "No hay sesgo"
    
num_aleatorios = [rd.randint(1,100) for i in range(50)]
num_moda = mode(num_aleatorios)
num_mediana = median(num_aleatorios)
num_media = mean(num_aleatorios)

resultados_sesgo = det_sesgo(num_moda,num_mediana,num_media)
print(f"Moda: {num_moda}, Mediana: {num_mediana}, Media: {num_media}")
print(resultados_sesgo)

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación

def termina_vocal(frase):
    vowals = ["a","e","i","o","u"]
    letra = frase[-1].lower()
    if letra in vowals:
        return frase + "!"
    else:
        return frase

frase_usuario = input("Escriba una frase: ")
resultado_frase = termina_vocal(frase_usuario)
print(resultado_frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee.

def opciones(opcion,nombre):
    if opcion == 1:
        return nombre.upper()
    elif opcion == 2:
        return nombre.lower()
    else:
        return nombre.title()

nombre_persona = input("Ingrese su nombre: ")
opcion_persona = int(input("Ingrese el número de la opción que desea: "))
resultado_opcion = opciones(opcion_persona,nombre_persona)
print(resultado_opcion)

# 9) clasificacion de un terremoto segun magnitud de Ritcher

def magnitud_ter(magnitud):
    if magnitud < 3:
        return "Muy leve (imperceptible)."
    elif magnitud >= 3 and magnitud < 4:
        return "Leve (ligeramente perceptible)."
    elif magnitud >= 4 and magnitud < 5:
        return  "Moderado (sentido por personas, pero generalmente no causa daños)."
    elif magnitud >= 5 and magnitud <6:
        return  "Fuerte (puede causar daños en estructurasdébiles). "
    elif magnitud >= 6 and magnitud < 7:
        return "Muy Fuerte (puede causar daños significativos)."
    else:
        return "Extremo (puede causar graves daños a gran escala)."

informe_magnitud = float(input("Ingrese la magnitud del terremoto: "))
resultado_magnitud = magnitud_ter(informe_magnitud)
print(resultado_magnitud)

# 10) preguntar al usuario en que hemisferio se encuentra N/S

def epoca_año(hemisferio,mes,dia):
        op1 = mes <= 3 or mes == 12 and dia >= 21 or dia <=20
        op2 = mes >= 3 or mes <= 6 and dia >=21 or dia <= 20
        op3 = mes >= 6 or mes <=9 and dia >= 21 or dia <= 20
        op4 = mes >= 9 or mes <= 12 and dia >= 21 or dia <= 20
        
        if hemisferio == "N" and op1:
            return "Invierno"
        elif hemisferio == "N" and op2:
            return "Primavera"
        elif hemisferio == "N" and op3:
            return "Verano"
        elif hemisferio == "N" and op4:
            return "Otoño"
        elif hemisferio == "S" and op1:
            return "Verano"
        elif hemisferio == "S" and op2:
            return "Otoño"
        elif hemisferio == "S" and op3:
            return "Invierno"
        elif hemisferio == "S" and op4:
            return "Primavera"
        else:
            return "Error: datos incorrectos."

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("ingrese el mes(1,12):"))
dia = int(input("Ingrese el dia(1,31):"))
resultado_epoca = epoca_año(hemisferio,mes,dia)
print(resultado_epoca)


