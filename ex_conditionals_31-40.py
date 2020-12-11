
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
