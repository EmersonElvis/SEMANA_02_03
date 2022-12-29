'''Implemente un programa recursivo que calcule la
potencia de un numero elevado a otro. Sabemos que
2n = 2n/2. 2n/2 donde n es un nro par; y
2n = 2(n-1)/2. 2(n-1)/2.2 si n es impar'''


#b^n = b^(n/2) × b^(n/2) si n es par.
#b^n = b^(n−1)/2 × b^(n−1)/2 × b si n es impar.

def potencia_recursiva(base,exponente):
    """ Precondición: n debe ser mayor o igual que cero.
        Devuelve: b\^n. """

    # Caso base
    if exponente <= 0:
        resultado_f=1
    else:
        # n par
        if exponente % 2 == 0:
            resultado_i = potencia_recursiva(base, exponente/2)
            resultado_f=resultado_i*resultado_i
        # n impar
        else:
            resultado_i = potencia_recursiva(base, (exponente-1)/2)
            resultado_f= resultado_i * resultado_i * base
    return resultado_f
    
print(potencia_recursiva(2,8))