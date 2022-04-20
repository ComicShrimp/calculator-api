from typing import List

from fastapi import FastAPI, HTTPException, Query

from calculator_api.functions import operacao_soma
from calculator_api.models import Resultado, Versao

app = FastAPI(
    title="Calculator API",
    description="Projeto destinado a ser utilizado no TCC de Eng. Computação",
    version="0.1.0",
)


@app.get("/")
async def versao() -> Versao:
    return Versao(versao=app.version)


@app.get("/soma", response_model=Resultado)
async def soma(numeros: List[float] = Query(None)) -> Resultado:
    try:
        return Resultado(resultado=operacao_soma(numeros=numeros))
    except TypeError:
        raise HTTPException(status_code=422, detail="Nenhum numero informado!")
