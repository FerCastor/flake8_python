from typing import List, Dict, Union


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def retorna_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {
            f'Agência: {self.agencia} - '
            f'Data: {self.dia} -> '
            f'Clientes atendidos: ': len(clientes_atendidos)
        }
        return estatistica
