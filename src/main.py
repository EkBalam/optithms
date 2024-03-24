from optithms.functions import funcion1
from optithms.algorithms.univariable import busqueda_exhaustiva, acotamiento_fase

if __name__ == "__main__":
    result = busqueda_exhaustiva(funcion1, 0.000000001, 5, 10)
    print(result)

    result = acotamiento_fase(funcion1, 0.6, 0.5)
    print(result)