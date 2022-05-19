from typing import List


def operacao_soma(numeros: List[float]) -> float:
    return sum(numeros)


def operacao_subtracao(numeros: List[float]) -> float:
    total = numeros[0]
    for numero in numeros[1:]:
        total -= numero

    return total
