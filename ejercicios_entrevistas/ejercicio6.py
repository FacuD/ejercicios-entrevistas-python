def es_palindromo(palabra: str) -> bool:
    return palabra == "".join(list(reversed(palabra)))


if __name__ == "__main__":
    print(es_palindromo("radar"))
    print(es_palindromo("palindromo"))
