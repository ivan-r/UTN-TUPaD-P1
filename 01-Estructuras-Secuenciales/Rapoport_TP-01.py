# Trabajo Poráctico 1: Estructuras secuanciales
# Ivan Rapoport


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

print("Hola Mundo!")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

nombre = input("Ingresá tu nombre: ")

print(f"Hola {nombre}!")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = int(input("Ingresá tu edad: "))
residencia = input("Ingresá tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

radio = float(input("Ingresa el radio del circulo: "))

pi = 3.14
area = pi * radio ** 2
perimetro = pi * radio * 2

print(f"El área del criculo es {area}")
print(f"El perímetro del criculo es {perimetro}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

segundos = int(input("Ingresá la cantidad de segundos: "))

horas = segundos / 3600

print(f"{segundos} equivalen a {horas} horas")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

numero = int(input("Ingresá un número: "))

print(f"{numero} x 1 = {numero}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

numero1 = float(input("Ingresá un número distinto de 0: "))
numero2 = float(input("Ingresá otro número distinto de 0: "))

print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: IMC = peso en kg / (altura en m)^2
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

altura = float(input("Ingresá tu altura (m): "))
peso = float(input("Ingresá tu peso (kg): "))

imc = peso / altura ** 2

print(f"Tu IMC es {imc}")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

celsius = float(input("Ingresá la temepratura en grados celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")


# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

numero1 = float(input("Ingresá el primer número: "))
numero2 = float(input("Ingresá el segundo número: "))
numero3 = float(input("Ingresá el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio es {promedio}")
