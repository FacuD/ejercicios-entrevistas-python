from typing import Union


def sum(lista: list[Union[int, float]]) -> float:
    """Dada una lista lista de numeros devuelve su suma

    Args:
        lista (array): Lista de numeros

    Returns:
        float: La suma de todos los numeros de la lista
    """
    result = 0
    [result := result + numero for numero in lista]
    return result


def multip(lista: list[Union[int, float]]) -> float:
    """Dada una lista lista de numeros devuelve el resultado de multiplicarlos entre si

    Args:
        lista (array): Lista de numeros

    Returns:
        float: El resultado de multiplicar todos los numeros de la lista
    """
    result = 1
    [result := result * numero for numero in lista]
    return result


if __name__ == "__main__":
    print(sum([1, 2, 3, 4]))
    print(sum([1, -2, 3, 4]))
    print(multip([1, 2, 3, 4]))
    print(sum([1, "string", 3, 4]))
