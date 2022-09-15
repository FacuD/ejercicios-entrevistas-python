def generar_n_caracteres(n: int, c: str) -> str:
    if n < 0:
        raise Exception("El primer parametro tiene que ser un numero positivo")
    return c * n


if __name__ == "__main__":
    print(generar_n_caracteres(5, "x"))
    print(generar_n_caracteres(2, "algo"))
    print(generar_n_caracteres(1, "prueba"))
    print(generar_n_caracteres(-2, "prueba"))
