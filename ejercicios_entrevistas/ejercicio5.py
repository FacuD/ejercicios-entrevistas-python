import string


def inversa(palabra: string) -> string:
    """Devuelve la inversa de una cadena de texto

    Args:
        palabra (string): Palabra a evaluar su inversa

    Returns:
        string: Inversa de la cadena de texto
    """
    return palabra[::-1]


if __name__ == "__main__":
    print(inversa("estoy probando"))
    print(inversa("algo"))
