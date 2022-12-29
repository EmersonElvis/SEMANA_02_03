'''Implemente la selección por orden como un programa: El algoritmo de selección por
orden acomoda la sucesión s1, . . . , sn en orden no decreciente, para ello encuentra primero
el elemento más pequeño, por ejemplo si, y lo coloca en el primer lugar intercambiando
s1 y si. después encuentra el algoritmo más pequeño en s2, . . . , sn, de nuevo digamos si, y
lo coloca en el segundo lugar intercambiando s2 y si. Continua hasta que la sucesión esté
ordenada.'''

lista=[5,2,4,1,7,8,9,3,0,34,-4,55]

def SeleccionOrden (list,tamaño_list,contador):
    if contador<tamaño_list:
        num_pequeño = list[contador]
        posicion = contador
        for i in range(contador+1,tamaño_list):
            if lista[i]<num_pequeño:
                num_pequeño = list[i]
                posicion = i
        list[contador],list[posicion]=list[posicion],list[contador]
        SeleccionOrden(list,tamaño_list,contador+1)


SeleccionOrden(lista,len(lista),0)
print(lista)