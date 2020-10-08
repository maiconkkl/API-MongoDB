from pydantic.main import BaseModel


class PaisT(BaseModel):
    CodigoBacen: int
    Nome: str


class UfT(BaseModel):
    CodigoIbge: int
    Nome: str
    Sigla: str
    Pais: PaisT


class MunicipioT(BaseModel):
    CodigoIbge: int
    Nome: str
    Uf: UfT


class EnderecoPrincipalT(BaseModel):
    t: str
    Logradouro: str
    Numero: str
    Complemento: str
    Bairro: str
    InformacoesPesquisa: list
    Cep: str
    Municipio: MunicipioT
