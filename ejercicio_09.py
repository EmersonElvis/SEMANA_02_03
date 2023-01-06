'''Implemente un programa recursivo que sume
dos números a + b. Considera que la suma
a+b = a + 1 + 1 + ...+ 1 (b veces)'''

def suma_recursiva(a,b):
    if a==0 and b!=0:
        suma=b+suma_recursiva(a,b-1)
    elif b==0 and a!= 0:
        suma=a
    elif a==0 and b==0:
        suma = 0
    else:
        suma = a+b+suma_recursiva(a,b-1)
        if b==1:
            return suma-a
    return suma
print(suma_recursiva(45,79))
