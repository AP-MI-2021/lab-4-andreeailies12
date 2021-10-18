def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def suma(l):
    """
    Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă.
    :param l: lista de numere intregi
    :return: suma celui mai mare numar din lista si cel mai mic
    """
    mic = l[0]
    mare = l[0]
    for i in range(len(l)):
        if l[i]>mare:
            mare = l[i]
        if l[i] < mic:
            mic = l[i]
    suma = mare + mic
    return suma


def test_suma():
    assert suma([10, -3, 25, -1, 3, 25, 18]) == 22


def suma_cifrelor(l):
    """
    Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de
la tastatură.
    :param l: o lista de numere intregi
    :return: numerele cu suma cifrelor  mai mare sau egala  decat un nr citit de la tastatura.
    """
    suma = 0
    while numar != 0:
        suma = suma + (numar % 10)
        numar = numar // 10
    return suma

def lista_suma_numere(l, valoare):
    """
    Determina numerele care au suma cifrelor numere mai mare sau egala decat o valoare intreaga
    :param l: lista de numere intregi
    :param valoare: o valoare intreaga
    :return:o noua lista de numere intregi
    """
    rezultat = []
    for i in range(len(l)):
        suma = suma_cifrelor(l[i])
        if suma >= valoare:
            rezultat.append(l[i])
    return rezultat

def test_suma_cifrelor():
    assert suma([123]) == 6
def test_lista_suma_numere():
    assert lista_suma_numere([25, 11, 10, 24, 39, 7]) == [25, 39]



def main():
    test_suma()
    test_suma_cifrelor()
    test_lista_suma_numere()
    l = []

    while True:
        print("1. Citire lista")

        print("3. Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă ")
        print("4. ")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "3":
            print(suma(l))
        elif optiune == "4":
            print(test_lista_suma_numere(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")


main()
