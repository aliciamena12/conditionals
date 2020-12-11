
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
