from optithms.functions import Lata, Funcion1
from optithms.algoritmos.univariable import BusquedaExhaustiva, FaseDeAcotamiento, acotamiento_fase

if __name__ == "__main__":

    be = BusquedaExhaustiva(Funcion1(), 10)

    print(f"{be} Clase callable ", be.ejecutar())

    result = acotamiento_fase(Funcion1(), 0.6, 0.5)
    print("AF Clase callable ", result)

    fa = FaseDeAcotamiento(Funcion1(), 0.6, 0.5)
    print(f"{fa} Clase callable ", fa.ejecutar())

    # result = BusquedaExhaustiva(Lata(), 10)
    # print("BE Lata Clase callable ", result)


    # lata = Lata()

    # print(lata(-2))

