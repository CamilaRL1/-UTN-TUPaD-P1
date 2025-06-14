#def inmprimir_hola_m():
#    print ("Holaa mundo") 
#inmprimir_hola_m()


#def saludar_usuario(nombre):
#    return f"Hola {nombre}!"

#nombre_usuario = input("Por favor ingresa tu nombre: ")
#saludo = saludar_usuario(nombre_usuario)
#print(saludo)


#def informacion_personal(nombre, apellido, edad, residencia):
#    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#nombre = input("Ingrese Nombre: ")
#apellido = input("Ingrese Apellido: ")
#edad = input("Ingrese Edad: ")
#residencia = input("Ingrese su lugar de residencia: ")

#informacion_personal(nombre, apellido, edad, residencia)


#import math

#def calcular_area_circulo(radio):
#    return math.pi * radio ** 2

#def calcular_perimetro_circulo(radio):
#    return 2 * math.pi * radio

#radio = float(input("Ingresa el radio del círculo: "))
#area = calcular_area_circulo(radio)
#perimetro = calcular_perimetro_circulo(radio)

#print(f"Área: {area:.2f}")
#print(f"Perímetro: {perimetro:.2f}")


#def segundos_a_horas(segundos):
#    return segundos / 3600

#segundos = int(input("Ingresa la cantidad de segundos: "))
#horas = segundos_a_horas(segundos)
#print(f"Equivale a {horas:.2f} horas.")


#def tabla_multiplicar(numero):
#    for i in range(1, 11):
#        print(f"{numero} x {i} = {numero * i}")

#numero = int(input("Ingresa un numero (1 al 10) para ver la tabla de multiplicar: "))
#tabla_multiplicar(numero)


#def operaciones_basicas(a, b):
#    suma = a + b
#    resta = a - b
#    multiplicacion = a * b
#    division = a / b if b != 0 else "Indefinido"
#    return (suma, resta, multiplicacion, division)

#a = float(input("Por favor ingresa el primer número: "))
#b = float(input("Por favor ingresa el segundo número: "))

#resultados = operaciones_basicas(a, b)
#print(f"Suma: {resultados[0]}")
#print(f"Resta: {resultados[1]}")
#print(f"Multiplicación: {resultados[2]}")
#print(f"División: {resultados[3]}")


#def calcular_imc(peso, altura):
#    return peso / (altura ** 2)

#peso = float(input("Ingresa tu peso (kg): "))
#altura = float(input("Ingresa tu altura (m): "))

#imc = calcular_imc(peso, altura)
#print(f"Tu IMC es: {imc:.2f}")


#def celsius_a_fahrenheit(celsius):
#    return celsius * 9/5 + 32

#celsius = float(input("Ingresa la temperatura en Celsius: "))
#fahrenheit = celsius_a_fahrenheit(celsius)
#print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")


def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio seria de: {promedio:.2f}")
