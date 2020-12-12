extra

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

#31. Leer un número entero y determina si es igual a 10.
num = int(input("Elige un número entero: "))
if num == 10:
    print("El número elegido es igual a 10.")
else:
    print("El número elegido no es igual a diez.")

#32. Leer un número entero y determinar si es múltiplo de 7.
num = int(input("Elige un número entero: "))
if num == int(num / 7) * 7:
    print("El número elegido es múltiplo de 7.")
else:
    print("El número elegido no es múltiplo de 7.")

#33. Leer un número entero y determinar si termina en 7. hola
num = int(input("Elige un número entero: "))
unidad = int(num % 10)

if unidad == 7:
    print("El número elegido termina en 7.")
else:
    print("El número elegido no termina en 7.")

#34. Leer un número entero menor que mil y determinar cuántos dígitos tiene.
num = int(input("Elige un número entero natural menor que mil: "))
if num >= 0 and num <= 999:
    if num >= 0 and num <= 9:
        print("El número elegido tiene 1 dígito.")
    elif num >= 10 and num <= 99:
        print("El número elegido tiene 2 dígitos.")
    else:
        print("El número elegido tiene 3 dígitos")
else:
    print("El número elegido no es menor que mil.")
    
#35. Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y luego
# mostrarlas en pantalla.
num = int(input("Elige un número entero de dos dígitos: "))
if num >= 10 and num <= 99:
    decenas = int(num / 10)
    unidad = int(num % 10)
    print(decenas)
    print(unidad)
else:
    print("El número elegido no tiene dos dígitos.")

#36. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.
num = int(input("Elige un número entero de cuatro dígitos: "))
millar = int(num / 1000)
centenas = int(num / 100) % 10
decenas = int(num / 10) % 10
unidad = int(num % 10)
pares = 0
impares = 0
if num >= 1000 and num <= 9999:
    if millar == int(millar/ 2) * 2:
        pares = pares + 1
    else:
        impares = impares + 1
    if centenas == int(centenas/ 2) * 2:
        pares = pares + 1
    else:
        impares = impares + 1
    if decenas == int(decenas/ 2) * 2:
        pares = pares + 1
    else:
        impares = impares + 1
    if unidad == int(unidad/ 2) * 2:
        pares = pares + 1
    else:
        impares = impares + 1
    print("El número elegido tiene " + str(pares) + " dígitos pares.")
    print("El número elegido tiene " + str(impares) + " dígitos impares.")
else:
    print("El número que has elegido no tiene cuatro dígitos.")

#37. Leer dos números enteros y determinar cuál es múltiplo de cuál.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
if num1 > num2:
    if num1 == int(num1 / num2) * num2:
        print("El primer número es múltiplo del segundo número.")
    else:
        print("Ningún número es múltiplo del otro.")
elif num2 > num1:
    if num2 == int(num2 / num1) * num1:
        print("El segundo número es múltiplo del primer número.")
    else:
        print("Ningún número es múltiplo del otro.")
else:
    print("Los dos números elegidos son iguales.")

#38. Leer tres números enteros y determinar si el último dígito de los tres números es igual.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un segundo número entero: "))
num3 = int(input("Elige un tercer número entero: "))
unidad1 = int(num1 % 10)
unidad2 = int(num2 % 10)
unidad3 = int(num3 % 10)

if unidad1 == unidad2 and unidad1 == unidad3:
    print("Los tres números tienen el mismo último dígito.")
elif unidad1 != unidad2 and unidad1 != unidad3 and unidad2 != unidad3:
    print("Ningun número coincide en el último dígito.")
else:
    if unidad1 == unidad2: 
        print("El primer número coincide en el último dígito con el segundo número.")
    if unidad2 == unidad3:
        print("El segundo número coincide en el último dígito con el tercer número.")   
    if unidad1 == unidad3:
        print("El primer número coincide en el último dígito con el tercer número.")

#39. Leer tres números enteros y determina si el penúltimo dígito de los tres números es igual.
num1 = int(input("Elige un número entero de dos o más dígitos: "))
num2 = int(input("Elige un segundo número entero de dos o más dígitos: "))
num3 = int(input("Elige un tercer número entero de dos o más dígitos: "))
decenas1 = int(num1 / 10) % 10
decenas2 = int(num2 / 10) % 10
decenas3 = int(num3 / 10) % 10
if num1 >= 10 and num2 >= 10 and num3 >= 10:
    if decenas1 == decenas2 and decenas1 == decenas3:
        print("Estos 3 números tienen el mismo penúltimo dígito.")
    else:
        print("Estos 3 números tienen diferente sus penúltimos dígitos.") 
else:
    print("No has elegido 3 números de dos o más digitos")

#40. Leer dos números enteros y si la diferencia entre los dos es menor o igual a 10 entonces
# mostrar en pantalla todos los enteros comprendidos entre el menor y el mayor de los números leídos.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un número entero: "))
resta = 0
if num1 > num2:
    resta = num1 - num2
elif num2 > num1:
    resta = num2 - num1
elif num1 == num2:
    resta == 0
else:
    None

if resta <= 10:
    if num1 < num2:
        while num1 < (num2 - 1):
            num1 = num1 + 1
            print(num1)
    elif num2 < num1:
        while num2 < (num1 - 1):
            num2 = num2 + 1
            print(num2)
    else:
        None
else:
    None

#41. Leer dos números enteros y determinar si la diferencia entre los dos es un número primo.
num1 = int(input("Elige un número entero: "))
num2 = int(input("Elige un número entero: "))
resta = 0
if num1 > num2:
    resta = num1 - num2
elif num2 > num1:
    resta = num2 - num1
elif num1 == num2:
    resta == 0
else:
    None
if resta != 0:
    if resta == int(resta / 2) * 2 and resta != 2:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 3) * 3 and resta != 3:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 5) * 5 and resta != 5:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 7) * 7 and resta != 7:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 11) * 11 and resta != 11:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 13) * 13 and resta != 13:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 17) * 17 and resta != 17:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 19) * 19 and resta != 19:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 23) * 23 and resta != 23:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 29) * 29 and resta != 29:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 31) * 31 and resta != 31:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 37) * 37 and resta != 37:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 41) * 41 and resta != 41:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 43) * 43 and resta != 43:
        print("La diferencia entre los dos números no es un número primo.")
    elif resta == int(resta / 47) * 47 and resta != 47:
        print("La diferencia entre los dos números no es un número primo.")
    else:
        print("La diferencia entre los dos números elegidos es un número primo.")
else:
    print("Los dos números elegidos son iguales.")

#42. Leer dos números enteros y determinar si la diferencia entre los dos es un número par.
num1 = int(input("Elige un número entero de dos o más dígitos: "))
num2 = int(input("Elige un segundo número entero de dos o más dígitos: "))
diferencia = num1 - num2
if diferencia == int(diferencia / 2) * 2:
    print("La diferencia entre los dos números es un número par.")
else:
    print("La diferencia entre los dos números es un número impar.")

#43. Leer dos números enteros y determinar si la diferencia entre los dos es un número divisor
#exacto de alguno de los dos números.
num1 = int(input("Elige un número entero de 4 dígitos: "))
num2 = int(input("Elige un número entero de 4 dígitos: "))
if num1 > num2:
    diferencia = num1 - num2
elif num2 > num1:
    diferencia = num2 - num1
else:
    print("Los dos números son iguales.")
if num1 == int(num1 / diferencia) * diferencia:
    print("La diferencia de los dos números es un número divisor del primer número.")
elif num2 == int(num2 / diferencia) * diferencia:
    print("La diferencia de los dos números es un número divisor del segundo número.")
else:
    print("La diferencia de los dos números no es número divisor de ninguno de los dos números.")

#44. Leer un número entero de 4 dígitos y determinar si el primer dígito es múltiplo de alguno de los otros dígitos.
# si no hay no pasa nada
num = int(input("Elige un número entero de 4 dígitos: "))
millar = int(num / 1000)
centenas = int(num / 100) % 10
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 1000 and num <= 9999:
    if millar == int(millar / centenas) * centenas:
        print("El primer dígito es múltiple del segundo dígito.")
    if millar == int(millar / decenas) * decenas:
        print("El primer dígito es múltiple del penúltimo dígito.")
    if millar == int(millar / unidad) * unidad:
        print("El primer dígito es multiple del último dígito.")
    if millar != int(millar / centenas) * centenas and millar != int(millar / decenas) * decenas and millar != int(millar / unidad) * unidad:
        print("Ningún dígito es múltiple de los otros.")
else:
    print("El número elegido no tiene 4 dígitos.")

#45. Leer un número entero de 2 dígitos y si es par mostrar en pantalla la suma de sus dígitos, si es
# primo y menor que 20 mostrar en pantalla su último dígito y si es múltiplo de 5 y menor que 30
# mostrar en pantalla el primer dígito.
num = int(input("Elige un número entero de 2 dígitos: "))
decenas = int(num / 10) % 10
unidad = int(num % 10)
if num >= 10 and num <= 100:
    if num == int(num / 2) * 2:
       suma = unidad + decenas
       print(suma)
    if num < 20:
        if num != int(num / 2) * 2 and num != int(num / 3) * 3 and num != int(num / 5) * 5:
            print(unidad)
        else:
            None
    if num < 30:
        if num == int(num / 5) * 5:
            print(decenas)
        else:
            None
else:
    print("El número elegido no tiene 2 dígitos.")

#46. Leer un número entero de 2 dígitos y si terminar en 1 mostrar en pantalla su primer dígito, si
# termina en 2 mostrar en pantalla la suma de sus dígitos y si termina en 3 mostrar en pantalla el
# producto de sus dos dígitos.
num = int(input("Elige un número entero de 2 dígitos: "))
unidad = int(num % 10)
decenas = int(num / 10)
if num >= 10 and num <= 100:
    if unidad == 1:
    print(decenas)
    elif unidad == 2:
    suma = unidad + decenas
    print(suma)
    elif unidad == 3:
    producto = unidad * decenas
    print(producto) 
else:
    print("El número elegido no tiene 2 dígitos.")

#47. Leer dos números enteros (de dos dígitos) y si la diferencia entre los dos números es par mostrar en pantalla la
# suma de los dígitos de los números, si dicha diferencia es un número primo menor que 10
# entonces mostrar en pantalla el producto de los dos números y si la diferencia entre ellos
# terminar en 4 mostrar en pantalla todos los dígitos por separado.
## No queda claro si la última condicion es mostrar los dígitos de la diferencia o de los números elegidos
num1 = int(input("Elige un número entero de dos dígitos: "))
num2 = int(input("Elige un segundo número entero de dos dígitos: "))
decenas1 = int(num1 / 10)
unidad1 = int(num1 % 10)
decenas2 = int(num2 /10)
unidad2 = int(num2 % 10)
suma = decenas1 + unidad1 + decenas2 + unidad2
producto = num1 * num2
if num1 >= 10 and num1 <= 99 and num2 >= 10 and num2 <= 99:
    if num1 < num2:
        resta = num2 - num1
    elif num2 < num1:
        resta = num1 - num2
    else:
        print("Los dos números elegidos son iguales.")
    unidadresta = int(resta % 10)
    if num1 != num2:
        if resta == int(resta / 2) * 2:
            print("La suma de todos los dígitos de los números es: " + str(suma))
        if resta <= 10:
            if num == int(num / 2) * 2 and num != 2:
                print("No es un número primo.")
            elif num == int(num / 3) * 3 and num != 3:
                print("No es un número primo.")
            else:
                print(producto)
        if unidadresta == 4:
            if resta >= 10 and resta <= 99:
                decenasresta = int(resta / 10)
                print(str(decenasresta) + ", " + str(unidadresta))
            else:
                print(resta)
else:
    print("No todos los números elegidos tienen dos dígitos.")

#48. Leer un número entero y si es menor que 100 determinar si es primo.
num = int(input("Elige un número entero menor a 100: "))
if num <= 99:
    if num == int(num / 2) * 2 and num != 2:
        print("No es un número primo.")
    elif num == int(num / 3) * 3 and num != 3:
        print("No es un número primo.")
    elif num == int(num / 5) * 5 and num != 5:
        print("No es un número primo.")
    elif num == int(num / 7) * 7 and num != 7:
        print("No es un número primo.")
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
    elif num == int(num / 29) * 29 and num != 29:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 31) * 31 and num != 31:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 37) * 37 and num != 37:
        print("El número que has elegido no es un número primo.")    
    elif num == int(num / 41) * 41 and num != 41:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 43) * 43 and num != 43:
        print("El número que has elegido no es un número primo.")
    elif num == int(num / 47) * 47 and num != 47:
        print("El número que has elegido no es un número primo.")
    else:
        print("Es un número primo.")
else:
    print("El número elegido no es menor a 100.")

#49. Leer un número entero y si es múltiplo de 4 determinar si su último dígito es primo.
num = int(input("Elige un número entero: "))
unidad = (num % 10)
if num == int(num / 4) * 4:
    if unidad == int(unidad / 2) * 2 and unidad != 2:
        print("El último dígito no es un número primo.")
    elif unidad == int(unidad / 3) * 3 and unidad != 3:
        print("El último dígito no es un número primo.")
    else:
        print("El último dígito es un número primo.")
else:
    print("El número que has elegido no es múltiplo de 4.")

#50. Leer un número entero y si es múltiplo de 4 mostrar en pantalla su mitad, si es múltiplo de 5
# mostrar en pantalla su cuadrado y si es múltiplo de 6 mostrar en pantalla su primer dígito.
# Asumir que el número no es mayor que 100.
num = int(input("Elige un número entero de dos dígitos menor a 100: "))
if num <= 99:
    if num == int(num / 4) * 4:
        print("La mitad del número elegido es: " + str(num / 2))
    elif num == int(num / 5) * 5:
        print("El número elegido al cuadrado es: " + str(num * num))
    elif num == int(num / 6) * 6:
        print(int(num / 10))
    else:
        print("El número elegido no es múltiplo de 4, 5 y 6.")
else:
    print("El número que has elegido es mayor a 100.")
