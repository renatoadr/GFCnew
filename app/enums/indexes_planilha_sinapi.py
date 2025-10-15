from enum import Enum


class IDX_PLAN_SINAPI(Enum):
    Codigo = 0
    Composicao = 1
    Unidade = 4
    Quantidade = 5
    Custo = 6
    QuantEng = 7
    Total = 9
    UnitSinapi = 8
    TotalSinapi = 10
    PercentDiff = 11

    NomeCliente = 'D1'
    Endereco = 'D2'
    Data = 'D3'
    DescTotalSinapi = 'E2'
    DescPercentDiff = 'E3'
    ValorTotal = 'G1'
    ValorTotalSinapi = 'G2'
    ValorPercentDiff = 'G3'
    NomeEmpreend = 'A5'
    CabecalhoTotal = 'J6'
    CabecalhoUnitSinapi = 'I6'
    CabecalhoTotalSinapi = 'K6'
    CabecalhoPercentDiff = 'L6'
