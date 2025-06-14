#def factorial(n):
#    if n == 0 or n == 1:
#        return 1
#    return n * factorial(n - 1)

#limite = int(input("Calcular factorial desde 1 hasta: "))
#for i in range(1, limite + 1):
#    print(f"{i}! = {factorial(i)}")
 


#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    return fibonacci(n - 1) + fibonacci(n - 2)

#pos = int(input("Mostrar la serie Fibonacci hasta la posición: "))
#print("Serie Fibonacci:")
#for i in range(pos + 1):
#    print(fibonacci(i), end=" ")



#def potencia(base, exponente):
#    if exponente == 0:
#        return 1
#    return base * potencia(base, exponente - 1)

#base = int(input("Base: "))
#exp = int(input("Exponente: "))
#print(f"{base}^{exp} = {potencia(base, exp)}")



#def decimal_a_binario(n):
#    if n == 0:
#        return ""
#    return decimal_a_binario(n // 2) + str(n % 2)

#numero = int(input("Convertir a binario (decimal): "))
#binario = decimal_a_binario(numero)
#print(f"{numero} en binario es: {binario if binario else '0'}")



#def es_palindromo(palabra):
#    if len(palabra) <= 1:
#        return True
#    if palabra[0] != palabra[-1]:
#        return False
#    return es_palindromo(palabra[1:-1])

#texto = input("Palabra sin espacios ni tildes: ").lower()
#print(f"¿Es palíndromo?: {es_palindromo(texto)}")



#def suma_digitos(n):
#    if n < 10:
#        return n
#    return (n % 10) + suma_digitos(n // 10)

#numero = int(input("Número para sumar sus dígitos: "))
#print(f"Suma de dígitos: {suma_digitos(numero)}")



#def contar_bloques(n):
#    if n == 1:
#        return 1
#    return n + contar_bloques(n - 1)

#niveles = int(input("Bloques en el nivel más bajo: "))
#print(f"Total de bloques necesarios: {contar_bloques(niveles)}")



#def contar_digito(numero, digito):
#    if numero == 0:
#        return 0
#    ultimo = numero % 10
#    if ultimo == digito:
#        return 1 + contar_digito(numero // 10, digito)
#    else:
#        return contar_digito(numero // 10, digito)

#n = int(input("Número entero positivo: "))
#d = int(input("Dígito a contar (0-9): "))
#print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")



