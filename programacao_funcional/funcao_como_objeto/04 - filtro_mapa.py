# Reutilizando a mesma lista do exercício anterior
alunos = [('Paulo', 0), ('Renzo', 10), ('Ada', 9)]

# Podemos usar uma list comprehension que faça as vezes de filtro para obter o resultado que queremos
print([(nome, nota) for nome, nota in alunos if nota > 5])


# o filter é uma função de alta ordem que recebe como primeiro parâmetro uma função que receberá elementos de um
# iterável que será passado como segundo parâmetro
def possui_nota_maior_que_5(aluno):
	_, nota = aluno
	return nota > 5

print(list(filter(possui_nota_maior_que_5, alunos)))
