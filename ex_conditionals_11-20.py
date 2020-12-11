a
#11. Leer dos números enteros y determinar cuál es el mayor.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige otro numero: "))
if num1 < num2
    print("El segundo número es mayor.")
elif num1 > num2:
    print("El primer número es mayor.")
else:
    print("Los dos dígitos son iguales.")

#12. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.--
num1 = int(input("Elige un número entero de dos dígitos: "))
num2 = int(input("Elige otro número entero de dos dígitos: "))
decenas1 = int(num1 / 10)
unidad1 = int(num1 % 10)
decenas2 = int(num2 / 10)
unidad2 = int(num2 % 10)
if num1 >= 10 and num1 <= 99 and num2 >= 10 and num2 <= 99:
    if decenas1 == decenas2 or decenas1 == unidad2 or unidad1 == decenas1 or unidad1 == unidad2:
        print("Estos números tienen dígitos en común.")
    else:
        print("Estos números no tienen dígitos en común.")
else:
    print("Los números que has elegido no valen.")

#13. Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par.
num1 = int(input("Elige un número entero de dos dígitos: "))
num2 = int(input("Elige otro número entero de dos dígitos: "))
suma = num1 + num2
if num1 >= 10 and num1 <= 99 and num2 >= 10 and num2 <= 99:
    if int(suma / 2) * 2 == suma:
        print("La suma de los números da un número par.")
    else:
        print("La suma de los números da un número impar.")
else:
    print("Los números que has elegido no valen.")

#14. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.
num1 = int(input("Elige un número entero de dos dígitos: "))
num2 = int(input("Elige otro número entero de dos dígitos: "))
decenas1 = int(num1 / 10)
unidad1 = int(num1 % 10)
decenas2 = int(num2 / 10)
unidad2 = int(num2 % 10)
suma = decenas1 + unidad1 + decenas2 + unidad2
if num1 >= 10 and num1 <= 99 and num2 >= 10 and num2 <= 99:
    print("La suma de todos los dígitos es: " + str(suma))
else:
    print("Los números que has elegido no valen.")

#15. Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.
num = int(input("Elige un número entero de 3 dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidades = int(num % 10)
suma = centenas + decenas + unidades
if num >= 100 and num <= 999:
    print("La suma de todos los dígitos es: " + str(suma))
else:
    print("El número elegido no tiene 3 dígitos.")

#16. Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.
num = int(input("Elige un número de 3 dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 100 and num <= 999:
    if centenas == unidad:
        print("El primer dígito del número es igual al último dígito.")
    elif decenas == unidad:
        print("El segundo dígito del número es igual al último dígito.")
    elif centenas == decenas:
        print("El primer dígito del número es igual al segundo dígito.")
    else:
        print("Ninguno de los dígitos es igual al resto.")
else:
    print("El número que has elegido no tiene 3 dígitos.")

#17. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
num = int(input("Elige un número de 3 dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 100 and num <= 999:
    if centenas > unidad and centenas > decenas:
        print("El primer dígito del número es el mayor dígito.")
    elif decenas > unidad and decenas > centenas:
        print("El segundo dígito del número es el mayor dígito.")
    elif unidad > decenas and unidad > centenas:
        print("El último dígito del número es el mayor dígito.")
    else:
        print("Los tres dígitos son iguales.")
else:
    print("El número que has elegido no tiene 3 dígitos.")

#18. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.
num = int(input("Elige un número entero de tres dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
nomultiplo = 0
if num >= 100 and num <= 999:
    if centenas == int(centenas / decenas) * decenas:
        print("El primer dígito es múltiplo del segundo dígito.")
    elif centenas == int(centenas / unidad) * unidad:
        print("El primer dígito es múltiplo del tercer dígito")
    elif centenas == int(centenas / decenas) * decenas and centenas == int(centenas / unidad) * unidad:
        print("El primer dígito es múltiplo del segundo y tercer dígito.")
    else:
        nomultiplo = nomultiplo + 1
    
    if decenas == int(decenas / centenas) * centenas:
        print("El segundo dígito es múltiplo del primer dígito.")
    elif decenas == int(decenas / unidad) * unidad:
        print("El segundo dígito es múltiplo del tercer dígito")
    elif decenas == int(decenas / centenas) * centenas and decenas == int(decenas / unidad) * unidad:
        print("El segundo dígito es múltiplo del primer y tercer dígito.")
    else:
        nomultiplo = nomultiplo + 1
    
    if unidad == int(unidad / centenas) * centenas:
        print("El tercer dígito es múltiplo del primer dígito.")
    elif unidad == int(unidad / decenas) * decenas:
        print("El tercer dígito es múltiplo del segundo dígito")
    elif unidad == int(unidad / centenas) * centenas and unidad == int(unidad / decenas) * decenas:
        print("El tercer dígito es múltiplo del primer y segundo dígito.")
    else:
        nomultiplo = nomultiplo + 1

    if nomultiplo == 3:
        print("Ningun dígito es múltiplo de los otros.")
else:
    print("El número elegido no tiene tres dígitos.")

#19. Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.
num1 = int(input("Elige un número de 3 dígitos: "))
num2 = int(input("Elige un segundo número de 3 dígitos: "))
num3 = int(input("Elige un tercer número de 3 dígitos: "))
if num1 >= 100 and num1 <= 999 and num2 >= 100 and num2 <= 999 and num3 >= 100 and num3 <= 999:
    if num1 > num2 and num1 > num3:
        print("El primer número es el mayor.")
    elif num2 > num1 and num2 > num3:
        print("El segundo número es el mayor.")
    else:
        print("El tercer número es el mayor.")
else:
    print("No todos los números tienen 3 dígitos.")

#20. Leer tres números enteros y mostrarlos ascendentemente.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
num3 = int(input("Elige un tercer número entero: "))
if num1 < num2 and num1 < num3:
    print(num1)
    if num2 < num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 < num1 and num2 < num3:
    print(num2)
    if num1 < num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 < num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
