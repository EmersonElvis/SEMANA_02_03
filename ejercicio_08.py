'''Implemente un programa recursivo que calcule la
potencia de un numero elevado a otro. Sabemos que
2n = 2n/2. 2n/2 donde n es un nro par; y
2n = 2(n-1)/2. 2(n-1)/2.2 si n es impar'''


def potencia_recursiva(base,exponente):
    """ Precondición: exponente debe ser mayor o igual que cero.
        Devuelve: base\^exponente. """

    # Caso base
    if exponente <= 0:
        resultado_f=1
    else:
        # exponente par
        if exponente % 2 == 0:
            resultado_i = potencia_recursiva(base, exponente/2)
            resultado_f=resultado_i*resultado_i
        # exponente impar
        else:
            resultado_i = potencia_recursiva(base, (exponente-1)/2)
            resultado_f= resultado_i * resultado_i * base
    return resultado_f
    
print(potencia_recursiva(2,8))
