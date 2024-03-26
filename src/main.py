from optithms.functions import funcion1, Lata, Funcion1
from optithms.algorithms.univariable import busqueda_exhaustiva, acotamiento_fase

if __name__ == "__main__":
    result = busqueda_exhaustiva(funcion1, 10, 0.001, 5)
    print("BE Funcion", result)

    result = busqueda_exhaustiva(Funcion1(), 10)
    print("BE Clase callable ", result)

    result = acotamiento_fase(funcion1, 0.6, 0.5)
    print("AF Funcion", result)

    result = acotamiento_fase(Funcion1(), 0.6, 0.5)
    print("AF Clase callable ", result)

    
    result = busqueda_exhaustiva(Lata(), 10)
    print("BE Lata Clase callable ", result)


    lata = Lata()

    print(lata(-2))

