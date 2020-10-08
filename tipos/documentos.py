from pydantic.main import BaseModel
from .endereco import UfT


class IeT(BaseModel):
    Numero: str
    Uf: UfT
