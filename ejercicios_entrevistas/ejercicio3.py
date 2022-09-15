import string
from xmlrpc.client import Boolean


def es_vocal(letra: string) -> Boolean:
    """Dado un carácter devuelve "True" si es una vocal o "False" si no lo es

    Args:
        letra (char): Letra a evaluar

    Raises:
        Exception: El parametro tiene que ser una letra y no una cadena de texto

    Returns:
        Boolean: El resultado de evaluar si la letra es una vocal o no
    """
    lista_vocales = ["a", "e", "i", "o", "u"]
    if len(letra) != 1:
        raise Exception("El parametro tiene que ser UNA letra")
    for vocal in lista_vocales:
        if vocal == letra:
            return True
    return False


if __name__ == "__main__":
    print(es_vocal("e"))
    print(es_vocal("s"))
    print(es_vocal("as"))
