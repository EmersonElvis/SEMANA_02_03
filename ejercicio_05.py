'''Escriba un programa recursivo y otro no recursivo para calcular
la sucesión de Fibonacci. Compare los tiempos requeridos
por los programas'''

import time
#Para recursivo
def fibonacci_recursivo(n):
    if n==0 or n==1:
        resultado=1
    else:
        resultado=fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    return resultado
tiempo_1=time.perf_counter()
recursivo=fibonacci_recursivo(20)
tiempo_2=time.perf_counter()
print(recursivo," Se hizo en: ", tiempo_2-tiempo_1)

#Para no recursivo
def fibonacci(n):
    iniciador_1=0
    iniciador_2=1
    for i in range(1,n+1):
        res=iniciador_2+iniciador_1
        iniciador_1=iniciador_2
        iniciador_2=res
    return iniciador_1

tiempo_1=time.perf_counter()
norecursivo=fibonacci(20)
tiempo_2=time.perf_counter()
print(norecursivo,"Se hizo en: ", tiempo_2-tiempo_1)