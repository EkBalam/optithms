import numpy as np

def busqueda_exhaustiva(funcion, a: float, b: float, n: int) -> tuple[float, float]:
    """Algoritmo de búsqueda exhaustiva

    Args:
        funcion (_type_): función a minimizar, debe ser univariable y retornar un valor flotante
        a (float): límite inferior de la función a minimizar
        b (float): límite superior de la función a minimizar
        n (int): número de puntos intermedios

    Returns:
        tuple[float, float]: intervalo donde se encuentra el mínimo
    """
    x1 = a
    delta_x = (b-a)/n
    x2 = x1 + delta_x
    x3 = x2 + delta_x
    while not (funcion(x1) >= funcion(x2) <= funcion(x3)) :
        x1, x2 = x2, x3
        x3 = x2 + delta_x
        if x3 > b:
            break
    return x1, x3


def acotamiento_fase(funcion, x: float, delta: float)-> tuple[float, float]:
    """Algoritmo de fase de acotamiento

    Args:
        funcion (_type_): función a minimizar, debe ser univariable y retornar un valor flotante
        x (float): punto inicial
        delta (float): incremento (positivo)

    Returns:
        tuple[float, float]: intervalo donde se encuentra el mínimo
    """
    if funcion( x - np.abs(delta)) <= funcion(x) <= funcion(x+np.abs(delta)) :
        delta *= -1
    
    k = 0
    x_k_menos1 = x
    x_k = x
    x_k_mas1 = x_k + (2**k) * delta
    
    while funcion(x_k_mas1) < funcion(x_k):
        print(x_k_menos1, x_k, x_k_mas1)
        x_k_menos1 = x_k
        x_k = x_k_mas1
        k += 1
        x_k_mas1 = x_k + (2**k) * delta
        
    return x_k_menos1, x_k_mas1
