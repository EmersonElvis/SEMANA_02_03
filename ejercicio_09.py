'''Implemente un programa recursivo que sume
dos números a + b. Considera que la suma
a+b = a + 1 + 1 + ...+ 1 (b veces)'''

def suma_recursiva(a,b):
    if a==0:
        suma=b
    else:
        if b==0:
            suma=a
        else:
            suma = a+suma_recursiva(a,b-1)
    return suma 
print(suma_recursiva(5,7))