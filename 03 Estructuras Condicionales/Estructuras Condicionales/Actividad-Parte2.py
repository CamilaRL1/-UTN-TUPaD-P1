#Actividad 6
#import random
#import statistics

#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#moda = statistics.mode(numeros_aleatorios)
#mediana = statistics.median(numeros_aleatorios)
#media = statistics.mean(numeros_aleatorios)

#print("Lista de números aleatorios:", numeros_aleatorios)
#print("Moda:", moda)
#print("Mediana:", mediana)
#print("Media:", media)

#if media > mediana > moda:
#    print("Hay sesgo positivo (asimetría a la derecha).")
#elif moda > mediana > media:
#    print("Hay sesgo negativo (asimetría a la izquierda).")
#else:
#    print("No hay sesgo (distribución simétrica).")

#Actividad 7 
#frase = input("Ingrese una frase o palabra: ")

#if frase[-1].lower() in "aeiou":
#    frase = frase + "!"  
#print(frase)

#Actividad 8
#nombre = input("Por facor ingrese su nombre: ")

#print("Elija una de las opciones:")
#print("1. Mostrar el nombre en mayúsculas")
#print("2. Mostrar el nombre en minúsculas")
#print("3. Mostrar el nombre con la primera letra en mayúscula")

#opcion = int(input("Ingrese el número de la opción deseada (1, 2 , 3): "))

#if opcion == 1:
#    print(nombre.upper())
#elif opcion == 2:
#    print(nombre.lower())
#elif opcion == 3:
#    print(nombre.title())
#else:
#    print("Opción inválida.")

#Actividad 9
#magnitud = float(input("Ingrese la magnitud del terremoto: "))

#if magnitud < 3:
#    print("Muy leve (imperceptible)")
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve (ligeramente perceptible)")
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado (sentido por personas, pero generalmente no causa daños)")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte (puede causar daños en estructuras débiles)")
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy Fuerte (puede causar daños significativos)")
#else:
#    print("Extremo (puede causar graves daños a gran escala)")

#Actividad 10
#hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
#mes = int(input("Ingrese el número de mes (1-12): "))
#dia = int(input("Ingrese el día del mes: "))

#if hemisferio == "N":
#    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#        print("Estación en el hemisferio norte: Invierno")
#    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#        print("Estación en el hemisferio norte: Primavera")
#    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#        print("Estación en el hemisferio norte: Verano")
#    else:
#        print("Estación en el hemisferio norte: Otoño")

#elif hemisferio == "S":
#    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
#        print("Estación en el hemisferio sur: Verano")
#    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
#        print("Estación en el hemisferio sur: Otoño")
#    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
#        print("Estación en el hemisferio sur: Invierno")
#    else:
#        print("Estación en el hemisferio sur: Primavera")
#else:
#    print("Hemisferio inválido. Por favor, ingrese N o S.")