from enum import Enum


class IDX_PLAN_SINAPI(Enum):
    Codigo = 0
    Composicao = 1
    Unidade = 4
    Quantidade = 5
    Custo = 6
    Total = 7
    UnitSinapi = 8
    TotalSinapi = 9
    PercentDiff = 10

    NomeCliente = 'D1'
    Endereco = 'D2'
    Data = 'D3'
    DescTotalSinapi = 'E2'
    DescPercentDiff = 'E3'
    ValorTotal = 'G1'
    ValorTotalSinapi = 'G2'
    ValorPercentDiff = 'G3'
    NomeEmpreend = 'A5'
    CabecalhoTotal = 'H6'
    CabecalhoUnitSinapi = 'I6'
    CabecalhoTotalSinapi = 'J6'
    CabecalhoPercentDiff = 'K6'
