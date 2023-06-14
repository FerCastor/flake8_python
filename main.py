from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica2 = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica2.atualiza_fila()
print(teste_fabrica.chama_cliente(3))
print(teste_fabrica2.chama_cliente(4))
print(teste_fabrica2.estatistica(EstatisticaDetalhada('20/10/2010', 200)))
print(teste_fabrica2.estatistica(EstatisticaResumida('20/10/2010', 200)))
