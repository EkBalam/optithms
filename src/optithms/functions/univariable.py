import numpy as np


def lata(radio:float) -> float:
    """
    Función para calcular el area de una lata para contener 250ml de liquido. 
    Basado en el radio de la lata.
    
    Sus limites son: 
        (0, 10], 0 < radio <= 10

    Args:
        radio (float): Radio de la lata

    Returns:
        float: area de la lata basada en el radio
    """
    operacion = 2 * np.pi * (radio**2)
    return operacion


def caja(l:float) -> float:
    """
    Se quiere construir una caja sin tapa a partir de una hoja de cartón de 20x10cm. 
    Para ello, se corta un cuadrado de lado L en cada esquina y se dobla la hoja levantando 
    los cuatro laterales de la caja.
    
    Determinar las dimensiones de la caja para que su volumen sea máximo si el lado 
    L debe medir entre 2 y 3 cm ( 2 ≤ L ≤ 3 ).

    Args:
        alto (float): alto L de la caja

    Returns:
        float: Volumen de la cada dado un L
    """
    return (20 - 2 * l) * (10 - 2 * l) * (l)


def funcion1(x:float) -> float:
    """
    .. math::
       f(x) = x^2+\frac{ 54  }{ x }
    
    Sus limites son: 
        (0, 10], 0 < x <= 10

    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (x**2) + (54/x)


def funcion2(x:float) -> float:
    """
    .. math::
       f(x) = x^3 + x^2 - 3

    Sus limites son: 
     (0, 5], 0 < x <= 5
       
    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (x**3) + (2*x) - 3

# Valores entre -2.5 o igual a 2.5
def funcion3(x:float) -> float:
    """
    .. math::
       f(x) = x^4 + x^2 - 33

    Sus limites son: 
     [-2.5, 2.5], -2.5 < x <= 2.5
       
    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (x**4) + (x**2) - 33


def funcion4(x:float) -> float:
    """
    .. math::
       f(x) = 3x^4 - 8x^3 - 6x^2 + 12x

    Sus limites son: 
     [-1.5, 3], -1.5 < x <= 3
       
    Args:
        x (float): variable dependiente

    Returns:
        float: valor de la función
    """
    return (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)