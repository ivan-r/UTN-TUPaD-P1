# Trabajo Poráctico 9: Análisis de algoritmos
# Ivan Rapoport

# Instrucciones:
#    1. Analiza cada algoritmo y determina su orden de complejidad T(n) y O(n).
#    2. Justifica tu respuesta indicando los pasos relevantes en el análisis.
#    3. En los ejercicios 1 y 2, compara ambas soluciones y argumenta cuál es más eficiente.

# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# Ejercicio 1: Suma de los primeros n números
# 
# def suma_numeros(n):
#     suma = 0
#     for i in range(1, n + 1):
#         suma += i
#     return suma
#
# Pregunta: ¿Cuál es el orden de complejidad de esta función? Explica tu respuesta.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

def suma_numeros(n): 
    suma = 0 # 1 operación
    for i in range(1, n + 1): # n iteraciones
        suma += i # 2 operaciones
    return suma # 1 operación

"""
    T(n) = 1 + 2n + 2 = 2n + 3  -> O(n)
"""

# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# Ejercicio 2: Suma de los primeros n números
#
# def suma_numeros_formula(n):
#    return (n * (n + 1)) // 2
#
# Pregunta: ¿Cuál es el orden de complejidad de esta función? ¿Cuál de las dos
# soluciones (Ejercicio 1 o 2) es más eficiente? Explica por qué.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

def suma_numeros_formula(n):
    return (n * (n + 1)) // 2 # 4 operaciones

"""
    T(n) = 1 -> O(1)

    La socluión del ejercicio 2 es más eficiente, ya que una función con orden de complejidad constante O(1) es 
    más eficiente que una con orden de complejidad lineal O(n)

"""

# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# Ejercicio 3: Búsqueda de un elemento en una lista desordenada
#
# def buscar_elemento(lista, objetivo):
#     for elemento in lista:
#         if elemento == objetivo:
#             return True
#     return False
#
# Pregunta: Determina el peor caso y la complejidad temporal de este algoritmo.
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

def buscar_elemento(lista, objetivo):
    for elemento in lista: # n iteraciones
        if elemento == objetivo: # 1 operación
            return True # 1 operación
    return False # 1 operación
    
"""
Complejidad temporal:
T(n) = 1n + 1

El peor caso es que el objetivo no esté contenido en la lista, por lo que se ejecutarán n + 1 operaciones
"""

# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# Ejercicio 4: Encontrar el número máximo en una lista
# 
# def encontrar_maximo(lista):
#     maximo = lista[0]
#     for elemento in lista:
#         if elemento > maximo:
#             maximo = elemento
#     return maximo
#
# Pregunta: ¿Cuál es el orden de complejidad de este algoritmo?
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

def encontrar_maximo(lista):
    maximo = lista[0] # 2 operaciones
    for elemento in lista: # n interaciones
        if elemento > maximo: # 1 operación
            maximo = elemento # 1 operación
    return maximo # 1 operación

"""
T(n) = 2 + 2n + 1 = 2n + 3 -> O(n)
"""

# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# Ejercicio 5: Ordenamiento por selección
#
# def ordenamiento_seleccion(lista):
#     n = len(lista)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#         if lista[j] < lista[min_idx]:
#            min_idx = j
#         lista[i], lista[min_idx] = lista[min_idx], lista[i]
#     return lista
#
# Pregunta: Determina la complejidad temporal de este algoritmo y explica su
# comportamiento en el peor caso
# •••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

def ordenamiento_seleccion(lista):
    n = len(lista) # 2 operaciones
    for i in range(n): # n iteraciones
        min_idx = i # 1 operación
        for j in range(i + 1, n): # n - 1 operaciones 
            if lista[j] < lista[min_idx]: # 3 operaciones
                min_idx = j # 1 operación
        lista[i], lista[min_idx] = lista[min_idx], lista[i] # 5 operaciones (6?)
    return lista # 1 operación

"""

T(n) = 2 + (1 + 4(n - 1) + 5)n + 1 = 4n^2 + 2n + 3

En el peor de los casos, estando la lista ordenada de forma descendiente, el indice del menor elemento se va 
a actualizar en cada iteración, sin emargo la complejidad espacial en el mejor y peor de los casos
es la mima O(n2)

"""