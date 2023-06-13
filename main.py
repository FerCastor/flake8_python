from fila_prioritaria import FilaPrioritaria

"""fila_teste = FilaNormal()
fila_teste.AtualizaFila()
fila_teste.AtualizaFila()
fila_teste.AtualizaFila()
print(fila_teste.ChamaCliente(5))
print(fila_teste.ChamaCliente(10))
print(fila_teste.ChamaCliente(2))"""


fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_clientes(10))
fila_teste2.atualiza_fila()
print(fila_teste2.chama_clientes(15))
print(fila_teste2.estatistica('10/10/2010', 197, 'detail'))
