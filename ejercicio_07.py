'''
Un robot puede dar pasos de 1, 2 o 3 metros. 
Escriba un programa para numerar todas las
maneras en que el robot camina n metros.'''

def robot_pasos(n):
    if n==1 or n==2 or n==3:
        resultado=n
    else:
        resultado=robot_pasos(n-1)+robot_pasos(n-2)+robot_pasos(n-2)
    return resultado

print(robot_pasos(6))