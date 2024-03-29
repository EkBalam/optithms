from optithms.functions import Lata, Funcion1
from optithms.algoritmos.univariable import BusquedaExhaustiva, FaseDeAcotamiento
from optithms.algoritmos.univariable import IntervalosMitad

if __name__ == "__main__":

    be = BusquedaExhaustiva(Funcion1(), 10)

    print(f"{be} Clase callable ", be.ejecutar())

    fa = FaseDeAcotamiento(Funcion1(), 0.6, 0.5)
    print(f"{fa} Clase callable ", fa.ejecutar())

    im = IntervalosMitad(Funcion1(), epsilon=10e-3)
    print(f"{im} Clase callable ", im.ejecutar())
