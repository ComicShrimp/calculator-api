from pydantic import BaseModel


class Resultado(BaseModel):
    resultado: float


class Versao(BaseModel):
    versao: str
