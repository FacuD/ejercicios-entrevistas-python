def validar_lista_numeros(lista) -> bool:
    """Dada una lista de elementos valida que todos sus elementos sean numeros

    Args:
        lista (array): Lista de numeros

    Returns:
        bool: Si todos los elementos de la lista son numeros o no
    """
    return all(isinstance(element, (int, float)) for element in lista)


def sum(lista) -> float:
    """Dada una lista lista de numeros devuelve su suma

    Args:
        lista (array): Lista de numeros

    Raises:
        Exception: Hay un elemento de la lista que no es un numero

    Returns:
        float: La suma de todos los numeros de la lista
    """
    if not validar_lista_numeros(lista):
        raise Exception("Alguno de los valores de la lista no es un numero")
    result = 0
    [result := result + numero for numero in lista]
    return result


def multip(lista) -> float:
    """Dada una lista lista de numeros devuelve el resultado de multiplicarlos entre si

    Args:
        lista (array): Lista de numeros

    Raises:
        Exception: Hay un elemento de la lista que no es un numero

    Returns:
        float: El resultado de multiplicar todos los numeros de la lista
    """
    if not validar_lista_numeros(lista):
        raise Exception("Alguno de los valores de la lista no es un numero")
    result = 1
    [result := result * numero for numero in lista]
    return result


if __name__ == "__main__":
    print(sum([1, 2, 3, 4]))
    print(sum([1, -2, 3, 4]))
    print(multip([1, 2, 3, 4]))
    print(sum([1, "string", 3, 4]))
