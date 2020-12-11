
#21. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
num1 = int(input("Elige un número de 2 dígitos: "))
num2 = int(input("Elige un segundo número de 2 dígitos: "))
num3 = int(input("Elige un tercer número de 2 dígitos: "))
decenas1 = int(num1 / 10)
unidad1 = int(num1 % 10)
decenas2 = int(num2 / 10)
unidad2 = int(num2 % 10)
decenas3 = int(num3 / 10)
unidad3 = int(num3 % 10)
if num1 >= 10 and num1 <= 99 and num2 >= 10 and num2 <= 99 and num3 >= 10 and num3 <= 99:
    if decenas1 > unidad1:
        grande1 = decenas1
    else:
        grande1 = unidad1
    if decenas2 > unidad2:
        grande2 = decenas2
    else:
        grande2 = unidad2    
    if decenas3 > unidad3:
        grande3 = decenas3
    else:
        grande3 = unidad3
    if grande1 > grande2 and grande1 > grande3:
        print("El primer número tiene el mayor dígito.")
    elif grande2 > grande1 and grande2 > grande3:
        print("El segundo número tiene el mayor dígito.")
    elif grande3 > grande1 and grande3 > grande2:
        print("El tercer número tiene el mayor dígito.")
    else:
        if grande1 == grande2:
            print("El primer número y el segundo tienen el dígito más alto.")
        elif grande2 == grande3:
            print("El segundo número y el tercero tienen el dígito más alto.")
        else:
            print("El primer número y el tercero tienen el dígito más alto.")
else:
    print("No todos los números tienen 2 dígitos.")

#22. Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último.
num = int(input("Elige un número de 3 dígitos: "))
centenas = int(num / 100)
unidad = int(num % 10)
if num >= 100 and num <= 999:
    if centenas == unidad:
        print("El primer dígito del número es igual al último.")
    else:
        print("El primer dígito del número no es igual al último.")
else:
    print("El número que has elegido no tiene 3 dígitos.")

#23. Leer un número entero de tres dígitos y determinar cuántos dígitos primos tiene.
num = int(input("Elige un número de 3 dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 100 and num <= 999:
    if centenas == int(centenas / 2) * 2 and centenas != 2:
        print("El primer dígito no es un número primo.")
    elif centenas == int(centenas / 3) * 3 and centenas != 3:
        print("El primer dígito no es un número primo.")
    elif centenas == int(centenas / 5) * 5 and centenas != 5:
        print("El primer dígito no es un número primo.")
    elif centenas == int(centenas / 7) * 7 and centenas != 7:
        print("El primer dígito no es un número primo.")
    else:
        print("El primer dígito es un número primo.")
    if decenas == int(decenas / 2) * 2 and decenas != 2:
        print("El segundo dígito no es un número primo.")
    elif decenas == int(decenas / 3) * 3 and decenas != 3:
        print("El segundo dígito no es un número primo.")
    elif decenas == int(decenas / 5) * 5 and decenas != 5:
        print("El segundo dígito no es un número primo.")
    elif decenas == int(decenas / 7) * 7 and decenas != 7:
        print("El segundo dígito no es un número primo.")
    else:
        print("El segundo dígito es un número primo.")
    if unidad == int(unidad / 2) * 2 and unidad != 2:
        print("El tercer dígito no es un número primo.")
    elif unidad == int(unidad / 3) * 3 and unidad != 3:
        print("El tercer dígito no es un número primo.")
    elif unidad == int(unidad / 5) * 5 and unidad != 5:
        print("El tercer dígito no es un número primo.")
    elif unidad == int(unidad / 7) * 7 and unidad != 7:
        print("El tercer dígito no es un número primo.")
    else:
        print("El tercer dígito es un número primo.")
else:
    print("El número que has elegido no vale.")

#24. Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene.
num = int(input("Elige un número entero de 3 dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
pares = 0
if num >= 100 and num <= 999:
    if centenas == int(centenas / 2) * 2:
        pares = pares + 1
    if decenas == int(decenas / 2) * 2:
        pares = pares + 1
    if unidad == int(unidad / 2) * 2:
        pares = pares + 1
    print("El número elegido tiene " + str(pares) + " dígitos pares.")
else:
    print("El número elegido no tiene 3 dígitos.")

#25. Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos.
num = int(input("Elige un número de 3 dígitos: "))
centenas = int(num / 100)
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 100 and num <= 999:
    if centenas == decenas + unidad:
        print("El primer dígito es la suma de los otros dos.")
    elif decenas == centenas + unidad:
        print("El segundo dígito es la suma de los otros dos.")
    elif unidad == centenas + decenas:
        print("El tercer dígito es la suma de los otros dos.")
    else:
        print("Ningún dígito es la suma de los otros dos.")
else:
    print("No todos los números tienen 3 dígitos.")

#26. Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus dígitos.
num = int(input("Elige un número de 4 dígitos: "))
unidad_millar = int(num / 1000)
centenas = int(num / 100) % 10
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 1000 and num <= 9999:
    suma = unidad_millar + centenas + decenas + unidad
    print("La suma de los dígitos del número elegido da: " + str(suma))
else:
    print("El número que has elegido no tiene 4 dígitos.")

#27. Leer un número entero de cuatro dígitos y determinar cuántos dígitos pares tiene.
num = int(input("Elige un número entero de cuatro dígitos: "))
millar = int(num / 1000)
centenas = int(num / 100) % 10
decenas = int(num / 10) % 10
unidad = int(num % 10)
digitopar = 0
if num >= 1000 and num <= 9999:
    if decenas == int(decenas / 2) * 2:
        digitopar = digitopar + 1
    if centenas == int(centenas / 2) * 2:
        digitopar = digitopar + 1        
    if millar == int(millar / 2) * 2:
        digitopar = digitopar + 1        
    if unidad == int(unidad / 2) * 2:
        digitopar = digitopar + 1  
    print("El número de dígitos pares es: " + str(digitopar))
else:
    print("El número que has elegido no es de cuatro dígitos.")

#28. Leer un número entero menor que 50 y positivo y determinar si es un número primo.
num = int(input("Elige un número positivo menor a 50: "))
if num >= 0 and num <= 50:
    if num == int(num / 2) * 2 and num != 2:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 3) * 3 and num != 3:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 5) * 5 and num != 5:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 7) * 7 and num != 7:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 11) * 11 and num != 11:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 13) * 13 and num != 13:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 17) * 17 and num != 17:
        print("El número que has elegido no es un número primo.")    
    elif num == int(num / 19) * 19 and num != 19:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 23) * 23 and num != 23:
        print("El número que has elegido no es un número primo.")
    else:
        print("El número que has elegido es un número primo.")
else:
    print("El número que has elegido no vale.")

#29. Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej. 15651, 59895.
num = int(input("Elige un número de 5 dígitos: "))
decenas_millar = int(num / 10000)
unidad_millar = int(num / 1000) % 10
centenas = int(num / 100) % 10
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 10000 and num <=99999:
    if decenas_millar == unidad and unidad_millar == decenas:
        print("El número elegido es capicúa.")
    else:
        print("El número que has elegido no es capicúa.")
else:
    print("El número que has elegido no tiene 5 dígitos.")

#30. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
num = int(input("Elige un número de 4 dígitos: "))
unidad_millar = int(num / 1000)
centenas = int(num / 100) % 10
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 1000 and num <=9999:
    if centenas == decenas:
        print("El segundo dígito del número es igual al penúltimo.")
    else:
        print("El segundo dígito del número no es igual al penúltimo.")
else:
    print("El número que has elegido no tiene 4 dígitos.")
