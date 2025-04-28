# Actividad 1
#for i in range(101):  
#    print(i)

#Actividad 2
#numero = int(input("Por favor introduce un número entero: "))
#cantidad_digitos = len(str(abs(numero)))  

#print(f"El número ingresado {numero} tiene {cantidad_digitos} dígitos.")

#Actividad 3
#inicio = int(input("Por favor introduzca el primer numero (valor inicial): "))
#fin = int(input("Por favor introduzca el segundo número (valor final): "))

#if inicio >= fin:
#    print("El primer número debe ser menor que el segundo.")
#else:
#    suma = sum(range(inicio + 1, fin))
#    print(f"La suma de los números entre {inicio} y {fin} es: {suma}")

#Actividad 4 
#suma_total = 0
#while True:
#    numero = int(input("Ingresa un número entero ( para terminar colocar el numero 0): "))
#    if numero == 0:
#        break
#    suma_total += numero

#print(f"La suma total de los números ingresados es : {suma_total}")

#Actividad 5
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento_usuario = int(input("Adivinar el número entre 0 y 9: "))
    intentos += 1
    
    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor, Intente nuevamente.")
    else:
        print("El número es menor, Intente nuevamente.")
