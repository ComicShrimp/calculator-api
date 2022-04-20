from typing import List

from fastapi import FastAPI, Query

from .models import Resultado

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"versao": "0.1.0"}


@app.get("/soma", response_model=Resultado)
async def soma(number: List[float] = Query(None)) -> Resultado:
    return Resultado(resultado=sum(number))
