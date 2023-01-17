"""
Construa uma função de ordenação que ordene os alunos por nota. Se houver empate em nota, o nokme deverá definir a ordem
>>> alunos = [('Paulo Vitor', 0), ('Paulo Santos', 0), ('Renzo', 10), ('Ada', 9)]
>>> alunos.sort(key=ordenar_por_nota_e_nome)
>>> alunos
[('Paulo Santos', 0), ('Paulo Vitor', 0), ('Ada', 9), ('Renzo', 10)]
"""


#Soluçãozinha bonita em que ele retorna 2 parametros pro key, que irá ordenar com base na ordem em que foram passadas
def ordenar_por_nota_e_nome(aluno):
	nome, nota = aluno
	return nota, nome

