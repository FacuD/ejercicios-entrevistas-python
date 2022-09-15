def superposicion(lista1, lista2) -> bool:
    for el1 in lista1:
        for el2 in lista2:
            if el1 == el2:
                return True
    return False


if __name__ == "__main__":
    print(superposicion([1, 2, 3], [5, 2, 7]))
    print(superposicion(["a", 2, "c"], [5, 7, 2.3]))
    print(superposicion(["aa", 1.3, "ccw"], ["aa", -9, -1.3]))
