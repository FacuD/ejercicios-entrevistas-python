from ejercicio1 import my_max


def max_de_tres(num1: float, num2: float, num3: float) -> float:

    """Dado 3 valores de entrada devuelve el mayor de ellos
      num1 > num2 > num3
      num1 > num2 && num2 > num3 => num1 > num3

    Args:
        num1 (float): Primer numero a comparar
        num2 (float): Segundo numero a comparar
        num3 (float): Tercer numero a comparar

    Returns:
        float: El mayor de los 3 numeros
    """
    aux = my_max(num1, num2)
    max = my_max(aux, num3)

    return max


if __name__ == "__main__":
    print(max_de_tres(3, 2, 1))
    print(max_de_tres(1, 2, 3))
    print(max_de_tres(1, 1, 1))
