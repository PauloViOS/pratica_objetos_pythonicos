# O módulo operator possui diversas funções que são muito comuns no dida a dia da programação
# Podemos ver essa lista ao importar esse módulo no console e ver o autocomplete ao digitarmos 'operator.'
# vamos ver um exemplo usando a função itemgetter pra pegar o primeiro elemento de um iterável

import operator


pegar_primeiro = operator.itemgetter(0)
print(pegar_primeiro([1,2]))
print(pegar_primeiro(['primeiro',2]))


# Vamos usar isso no exemplo da aula anterior. Com essa função, não teremos que construir um método para extrair
# apenas o nome de um aluno

alunos = [('Paulo', 0), ('Renzo', 10), ('Ada', 9)]

def possui_nota_maior_que_5(aluno):
	_, nota = aluno
	return nota > 5


# Obtemos o mesmo resultado da aula anterior
print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))
