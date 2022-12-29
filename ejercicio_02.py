''' corra el algoritmo anterior "desordena"  (del ejercicio 1)
muchas veces para la misma sucesión de entrada.
¿Como puede analizarse la salida para determinar si es
verdaderamente “aleatorio”?
''' 
import random

lista=[1,3,4,5,6,7,8,9,0]

def desordenar (list,tamaño_list,contador):
    if contador<tamaño_list:
        numero=random.randint(contador,tamaño_list-1)
        list[contador],list[numero]=list[numero],list[contador]
        desordenar(list,tamaño_list,contador+1)
    
for i in range (1,5):
    desordenar(lista,len(lista),0)
    print(lista)
print("------------------------------------------------------------")
print('''Cuando ejecutamos varias veces el algoritmo, vemos
diferentes respuestas, entonces si es verdad aleatorio''')