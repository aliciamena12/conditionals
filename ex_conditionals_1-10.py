
#1. Leer un número entero y determinar si es un número terminado en 4.
num = float(input("Elige un número: "))
unidad = int(num % 10)
unidad2 = int(num % 100)
if num >=10 and num <= 99:
    if unidad == int(4):
        print("El número termina en 4.")
    else:
        print("El número no termina en 4.")
elif num >= 0 and num <= 9:
    if num == int(4):
        print("El número termina en 4.")
    else:
        print("El número no termina en 4.")
elif num >= 100 and num <= 999:
    if unidad2 == int(4):
        print("El número termina en 4.")
    else:
        print("El número no termina en 4.")
else:
    print("Elige otro número por favor.")

#2. Leer un número entero y determinar si tiene 3 dígitos.
num = str(input("Elige un número entero: "))
if num >=100 and num >= 999:
    print("El número elegido tiene 3 dígitos.")
else:
    print("El número elegido no tiene 3 dígitos.")

#3. Leer un número entero y determinar si es negativo.
num = float(input("Elige un número: "))
if num > 0:
    print("El número que has elegido es positivo.")
else:
    print("El número que has elegido no es positivo.")

#4. Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.
num = int(input("Elige un número entero de dos dígitos: "))
if num >= 10 and num <= 99:
    decenas = int(num / 10)
    unidad = int(num % 10)
    suma = decenas + unidad
    print(suma)
else:
    print("El número que has elegido no es de dos dígitos.")

#5. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
num = int(input("Elige un número entero de dos dígitos: "))
if num >= 10 and num <= 99:
    decenas = int(num / 10)
    unidad = int(num % 10)
    if int(decenas / 2) * 2 == decenas and int(unidad / 2) * 2 == unidad:
        print("Ambos dígitos son pares.")
    elif int(decenas / 2) * 2 == decenas or int(unidad / 2) * 2 == unidad:
            print("Solo un dígito es par.")
    else:
        print("Ningún dígito es par.")
else:
    print("El número que has elegido no es de dos dígitos.")

#6. Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
num = int(input("Elige un número entero de dos dígitos menor a 20: "))
if num >= 10 and num <= 20:
    if num == int(num / 2) * 2 and num != 2:
        print("No es un número primo.")
    elif num == int(num / 3) * 3 and num != 3:
        print("No es un número primo.")
    elif num == int(num / 5) * 5 and num != 5:
        print("No es un número primo.")
    elif num == int(num / 7) * 7 and num != 7:
        print("No es un número primo.")
    else:
        print("Es un número primo.")
else:
    print("El número que has elegido no vale.")

#7. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
num = int(input("Elige un número entero de dos dígitos: "))
if num >= 10 and num <= 99:
    print("El número que has elegido es positivo.")
    if num == int(num / 2) * 2 and num != 2:
        print("No es un número primo.")
    elif num == int(num / 3) * 3 and num != 3:
        print("No es un número primo.")
    elif num == int(num / 5) * 5 and num != 5:
        print("No es un número primo.")
    elif num == int(num / 7) * 7 and num != 7:
        print("No es un número primo.")
    else:
        print("Es un número primo.")
elif num <= -10 and num >= -99:
    print("El número escogido es negativo.")
    if num == int(num / 2) * 2 and num != 2:
        print("No es un número primo.")
    elif num == int(num / 3) * 3 and num != 3:
        print("No es un número primo.")
    elif num == int(num / 5) * 5 and num != 5:
        print("No es un número primo.")
    elif num == int(num / 7) * 7 and num != 7:
        print("No es un número primo.")
    else:
        print("Es un número primo.")
else:
    print("El número que has elegido no vale.")

#8. Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos. #########################
num = int(input("Elige un número entero de dos dígitos: "))
decenas = int(num / 10)
unidad = int(num % 10)
if num >= 10 and num <= 99:
    if decenas == int(decenas / 2) * 2 and decenas != 2:
        print("El primer dígito no es un número primo.")
    elif decenas == int(decenas / 3) * 3 and decenas != 3:
        print("El primer dígito no es un número primo.")
    elif decenas == int(decenas / 5) * 5 and decenas != 5:
        print("El primer dígito no es un número primo.")
    elif decenas == int(decenas / 7) * 7 and decenas != 7:
        print("El primer dígito no es un número primo.")
    else:
        print("El primer dígito es un número primo.")
    
    if unidad == int(unidad / 2) * 2 and unidad != 2:
        print("El segundo dígito no es un número primo.")
    elif unidad == int(unidad / 3) * 3 and unidad != 3:
        print("El segundo dígito no es un número primo.")
    elif unidad == int(unidad / 5) * 5 and unidad != 5:
        print("El segundo dígito no es un número primo.")
    elif unidad == int(unidad / 7) * 7 and unidad != 7:
        print("El segundo dígito no es un número primo.")
    else:
        print("El segundo dígito es un número primo.")
else:
    print("El número que has elegido no vale.")

#9. Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.
num = int(input("Elige un número entero de dos dígitos: "))
decenas = int(num / 10)
unidad = int(num % 10)
if num >= 10 and num <= 99:
    if decenas >= unidad and decenas == int(decenas / unidad) * unidad:
        print("El primer dígito es múltiplo del segundo.")
    elif unidad >= decenas and unidad == int(unidad / decenas) * decenas:
        print("El segundo dígito es múltiplo del primero.") 
    else:
        print("No son múltiples.")
else:
    print("El número que has elegido no vale.")

#10. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
num = int(input("Elige un número entero de dos dígitos: "))
decenas = int(num / 10)
unidad = int(num % 10)
if num >= 10 and num <= 99:
    if decenas == unidad:
        print("Los dos dígitos son iguales.")
    else:
        print("Los dos dígitos no son iguales.")
else:
    print("El número que has elegido no tiene dos dígitos.")
