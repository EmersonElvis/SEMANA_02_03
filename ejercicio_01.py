''' implemente el siguiente algoritmo como 
programa para desordenar. 
desordena (a,n){
    for i = 1 to n -1
        swap(ai, arand(i,n))
}
''' 

import random

lista=[1,3,4,5,6,7,8,9,0]

def desordenar (list,tamaño_list,contador):
    if contador<tamaño_list:
        numero=random.randint(contador,tamaño_list-1)
        list[contador],list[numero]=list[numero],list[contador]
        desordenar(list,tamaño_list,contador+1)

desordenar(lista,len(lista),0)
print(lista)
