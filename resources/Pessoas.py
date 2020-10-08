import json
import datetime
from bson.objectid import ObjectId
from tipos.endereco import *
from tipos.documentos import *
from database.Database import Database
from bson.json_util import dumps
from typing import Optional, Union


class CarteiraT(BaseModel):
    EnderecoPrincipal: EnderecoPrincipalT
    Celulares: list
    EmailsNfe: list
    Veiculos: list
    Ie: IeT


class ClienteT(BaseModel):
    LimiteCredito: float
    DataUltimaVenda: datetime.datetime
    TabelaPrecoReferencia: str
    FormaPagamentoReferencia: str
    VendedorReferencia: str


class ClassificacaoT(BaseModel):
    t: str


class Pessoa(BaseModel):
    uid: str
    t: list
    InformacoesPesquisa: list
    Versao: str
    Ativo: bool
    Nome: str
    Imagem: bytes
    DiaAcerto: int
    Carteira: CarteiraT
    Cliente: ClienteT
    Classificacao: ClassificacaoT
    NomeFantasia: Optional[str]
    Cnpj: Optional[str]
    Cpf: Optional[str]
    RegistroMunicipal: Optional[str]
    RamoAtividade: Optional[str]
    RegimeTributario: Optional[str]
    CNAE: Optional[str]
    Sistema: Optional[dict]
    Municipio: MunicipioT
    Endereco: str


@app.get("/pessoas/")
def pessoas():
    database = Database()
    database_server = database.database_server()
    collection = database_server["Pessoas"]
    data = []
    cursor = collection.find({})
    x = 0
    try:
        for doc in cursor:
            data.append(json.loads(dumps(doc)))
            x += 1
    finally:
        database.close_connection()
    return data


@app.get("/pessoas/{uid}")
def read_pessoa(uid: str):
    database = Database()
    database_server = database.database_server()
    collection = database_server["Pessoas"]
    data = []
    try:
        cursor = collection.find_one({"_id": ObjectId(uid)})
        data.append(json.loads(dumps(cursor)))
    finally:
        database.close_connection()
    return data