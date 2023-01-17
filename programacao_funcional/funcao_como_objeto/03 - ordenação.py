# Funções de alta ordem são utilizadas em diversas bibliotecas embutidas para simplificar a vida
alunos = [('Paulo', 0), ('Renzo', 10), ('Ada', 9)]

# A classe List possui um método de alta ordem que recebe como parâmetro key uma função que determina qual o critério
# de ordenação
alunos.sort(key=lambda aluno: aluno[1])
print('Ordenação por nota:')
print(alunos)


# Usamos acima uma função anônima. Como a única diferença entre uma função anônima e uma nomeada é o atributo
# __name__, podemos naturalmente usar uma função nomeada como key. Faremos isso abaixo
def por_nome(aluno):
	return aluno[0]


# sorted cria uma nova lista ao invés de ordenar a lista original
print('Ordenação por nome:')
print(sorted(alunos, key=por_nome))
