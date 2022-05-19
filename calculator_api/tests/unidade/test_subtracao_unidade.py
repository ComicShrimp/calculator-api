import pytest

from calculator_api.functions import operacao_subtracao


def test_numeros_positivos() -> None:
    numeros = [2.0, 2.0]
    assert operacao_subtracao(numeros=numeros) == 0


def test_numeros_negativos() -> None:
    numeros = [-2.0, -2.0]
    assert operacao_subtracao(numeros=numeros) == 0


def test_numeros_negativos_e_positivos() -> None:
    numeros = [-2.0, 2.0]
    assert operacao_subtracao(numeros=numeros) == -4


def test_erro_string() -> None:
    numeros = ["texto", -2.0]
    with pytest.raises(TypeError):
        operacao_subtracao(numeros=numeros)  # type: ignore
