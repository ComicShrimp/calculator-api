from calculator_api.functions import operacao_soma


def test_soma_numeros_positivos() -> None:
    numeros = [2.0, 2.0]
    assert operacao_soma(numeros=numeros) == 4
