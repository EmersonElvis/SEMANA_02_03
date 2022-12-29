'''Un robot puede dar pasos de 1 o 2 metros. 
Escriba un programa para numerar todas las
maneras en que el robot camina n metros.'''

def robot_pasos(n):
    if n==1 or n==2:
        resultado=n
    else:
        resultado=robot_pasos(n-1)+robot_pasos(n-2)
    return resultado

print(robot_pasos(7))