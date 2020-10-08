import datetime
from typing import Optional
from pydantic.main import BaseModel
from tipos.documentos import IeT
from tipos.endereco import EnderecoPrincipalT, MunicipioT


class CarteiraT(BaseModel):
    EnderecoPrincipal: EnderecoPrincipalT
    Celulares: list
    EmailsNfe: list
    Veiculos: list
    Ie: IeT


class ClienteT(BaseModel):
    LimiteCredito: float
    DataUltimaVenda: Optional[datetime.datetime]
    TabelaPrecoReferencia: Optional[str]
    FormaPagamentoReferencia: Optional[str]
    VendedorReferencia: Optional[str]


class ClassificacaoT(BaseModel):
    t: str


class IndicadorIeDestinatarioT(BaseModel):
    t: str


class RegimeTributarioT(BaseModel):
    t: str


class RamoAtividadeT(BaseModel):
    t: str
    TipoMesaContaCliente: int


class PontoDeVendaT(BaseModel):
    Ecfs: list
    Sats: list
    AssinaturaAplicativoComercial: str


class IndicadorOperacaoConsumidorFinalT(BaseModel):
    t: str
    Codigo: int
    Descricao: str


class PessoaT(BaseModel):
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
    RamoAtividade: Optional[RamoAtividadeT]
    RegimeTributario: Optional[RegimeTributarioT]
    CNAE: Optional[str]
    Sistema: Optional[dict]
    Municipio: Optional[MunicipioT]
    Endereco: Optional[str]


class PessoaMovimentacaoT(BaseModel):
    _t: str
    PessoaReferencia: str
    Nome: str
    Classificacao: ClassificacaoT
    EnderecoPrincipal: EnderecoPrincipalT
    Cliente: ClienteT
    IndicadorOperacaoConsumidorFinal: IndicadorOperacaoConsumidorFinalT
    Documento: str
    Ie: str
    IndicadorIeDestinatario: IndicadorIeDestinatarioT
    TelefonePrincipal: str
    EmailPrincipal: str
    InformacoesPesquisa: list
    EmailsNfe: list
    Rntrc: str
    Celulares: str
    NomeFantasia: str
    RegistroMunicipal: str
    Cnae: str
    RegimeTributario: Optional[RegimeTributarioT]
    RamoAtividade: Optional[RamoAtividadeT]
    PontoDeVenda: Optional[PontoDeVendaT]
    IsMatriz: Optional[bool]
    IncentivadorCultural: Optional[bool]
    RegimeEspecialTributacao: Optional[int]
    RegimeEspecialTributacao: Optional[bool]
