from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def retorna_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {
            'dia': self.dia, 'agencia': self.agencia,
            'clientes_atendidos': clientes_atendidos,
            'qtd_clientes_atendidos': (
                len(clientes_atendidos))
        }
        return estatistica
