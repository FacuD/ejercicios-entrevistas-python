def my_max(num1: float, num2: float) -> float:
    """Dado 2 numeros de entrada devuelve el mayor de ellos.

    Args:
        num1 (float): Primer numero a comparar
        num2 (float): Segundo numero a comparar

    Raises:
        Exception: "Los 2 numeros no pueden tener el mismo valor"

    Returns:
        float: El mayor de ambos numeros
    """
    if num1 == num2:
        raise Exception("Los parametros no pueden tener el mismo valor")
    if num1 > num2:
        return num1
    return num2


if __name__ == "__main__":
    print(my_max(1, 2))
    print(my_max(2, 1))
    print(my_max(1, 1))
