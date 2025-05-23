# Trabajo Poráctico 4: Estructuras repetitivas
# Ivan Rapoport

# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

for x in range(101):
    print(x)


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

num = int(input("Ingrese un número entero: "))
num2 = num
digitos = 1

num2 = num2 // 10

while num2 > 0:
    digitos += 1
    num2 = num2 // 10

d = "dígito" if digitos == 1 else "dígitos"
print(f"El número {num} tiene {digitos} {d}.")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

sum = 0

for n in range(num1 + 1, num2):
    sum += n

print(f"La suma es: {sum}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

sum = 0
num = int(input("Ingrese el primer número (0 para terminar): "))

while num != 0:
    sum += num
    num = int(input("Ingrese el siguiente número (0 para terminar): "))

print(f"La suma es: {sum}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

import random

MIN = 1
MAX = 9
intentos = 0
numero = random.randint(MIN, MAX)
num = MIN - 1

while num != numero:
    intentos += 1
    num = int(input("Adivine el número entre 0 y 9: "))

print(f"Fueron necesarios {intentos} intentos")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

for n in range(100, -1, -1):
    print(n)


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

num = int(input("Ingrese un número entero positivo: "))

if num > 0:
    sum = 0
    for n in range(num + 1):
        sum += n
    print(f"La sumatoria de 0 a {num} es {sum}")
else:
    print("El número debe ser entero positivo.")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

CANT = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

for n in range(CANT):
    num = int(input(f"Ingrese el número {n + 1}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

CANT = 10
media = 0

for n in range(CANT):
    num = float(input(f"Ingrese el número {n + 1}: "))
    media += num / CANT

print(f"La media es: {media}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

num = int(input("Ingrese un número: "))

if num >= 10:
    res = 0

    while num > 0:
        res *= 10
        res += num % 10
        num //= 10

    print(res)
else:
    print(num)