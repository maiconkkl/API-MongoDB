import datetime
from pydantic import BaseModel
from typing import List


class JuroT(BaseModel):
    t: str
    Codigo: int
    Descricao: str
    Percentual: float
    DiasCarencia: int


class MultaT(BaseModel):
    Percentual: float
    DiasCarencia: int


class SituacaoT(BaseModel):
    t: str
    Codigo: int


class EspeciePagamentoFieldT(BaseModel):
    t: str


class EspeciePagamentoDictT(BaseModel):
    t: str
    Codigo: int
    Descricao: str
    EspecieRecebimento: EspeciePagamentoFieldT


class HistoricoT(BaseModel):
    t: str
    Valor: float
    EspeciePagamento: EspeciePagamentoDictT
    PlanoContaCodigoUnico: str
    CentroCustoCodigoUnico: str
    ContaReferencia: str
    EmpresaReferencia: str
    NomeUsuario: str
    Data: datetime.datetime
    ChequeReferencia: str


class ParcelaT(BaseModel):
    t: str
    _id: str
    InformacoesPesquisa: List[str]
    Versao: str
    Ativo: bool
    Ordem: int
    Descricao: str
    Documento: str
    PessoaReferencia: str
    Vencimento: datetime.datetime
    Historico: List[HistoricoT]
    Situacao: SituacaoT
    ContaReferencia: str
    EmpresaReferencia: str
    NomeUsuario: str
    DataQuitacao: datetime.datetime
    Juro: JuroT
    Multa: MultaT
    Referencia: int
