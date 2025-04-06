edad = int(input("Introducir edad:"))

if edad >= 0 and edad <= 12:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres un adolecente")
elif edad >=18 and edad <=64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
