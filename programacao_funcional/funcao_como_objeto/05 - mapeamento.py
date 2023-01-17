# Muito parecido com o exemplo anterior. A diferença é que vamos tentar pegar apenas o nome do aluno que passa na
# filtragem
alunos = [('Paulo', 0), ('Renzo', 10), ('Ada', 9)]

# Podemos usar uma list comprehension que faça as vezes de filtro para obter o resultado que queremos
print([nome for nome, nota in alunos if nota > 5])


def possui_nota_maior_que_5(aluno):
	_, nota = aluno
	return nota > 5


print(list(filter(possui_nota_maior_que_5, alunos)))


# map tem uma assinatura muito parecida com a do filter. Recebe uma função que será usada em cada um dos elementos de
# um iterável que será passado como segundo parâmetro
def extrair_nome(aluno):
	nome, _ = aluno
	return nome


print(list(map(extrair_nome, filter(possui_nota_maior_que_5, alunos))))
