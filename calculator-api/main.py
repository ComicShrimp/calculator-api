from typing import List

from fastapi import FastAPI, HTTPException, Query

from .functions import operacao_soma
from .models import Resultado

app = FastAPI(
    title="Calculator API",
    description="Projeto destinado a ser utilizado no TCC de Eng. Computação",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict:
    return {"versao": app.version}


@app.get("/soma", response_model=Resultado)
async def soma(numeros: List[float] = Query(None)) -> Resultado:
    try:
        return Resultado(resultado=operacao_soma(numeros=numeros))
    except TypeError:
        raise HTTPException(status_code=422, detail="Nenhum numero informado!")
