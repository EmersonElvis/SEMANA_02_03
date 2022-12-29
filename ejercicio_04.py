'''Escriba un programa recursivo y otro no recursivo 
para calcular n!. Compare los tiempos
requeridos por los programas.'''

import time
#Para recursivo
def factorial_recursivo(n):
    if n==1:
        resultado=1
    else:
        resultado = n*factorial_recursivo(n-1)
    return resultado
tiempo_1 = time.perf_counter()
recursivo = factorial_recursivo(9)
tiempo_2 = time.perf_counter()
print(recursivo," Se hizo en: ", tiempo_2-tiempo_1)

#Para no recursivo
def factorial(n):
    iniciador = 1
    for i in range(n,1,-1):
        iniciador = iniciador*i
    return iniciador
tiempo_1 = time.perf_counter()
norecursivo = factorial(9)
tiempo_2 = time.perf_counter()
print(norecursivo," Se hizo en: ", tiempo_2-tiempo_1)