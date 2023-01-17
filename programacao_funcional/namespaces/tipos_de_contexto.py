a = 5


def f(a=3):
	# cria uma variável de escopo local
	b = 3
	# mostra todas as variáveis/funções acessíveis que possuem um escopo global
	print(globals())
	# mostra todas as variáveis/funções acessíveis que possuem um escopo local
	print(locals())
	# mostra o valor de a. A função busca pela variável com o nome definido no escopo mais próximo possível. Nesse
	# caso, como temos um 'a'' no escopo local e um no global, a função dará 'preferência' àquela 'a' do escopo local.
	# Se não tivéssemos passado o a como argumento da função f, não daria erro na função, pois ela buscaria o valor
	# de 'a' no escopo global, onde o valor é '5'
	print(a)
	# mostra o valor da variável de escopo local
	print(b)


# classes também criam seus próprios escopos, como demonstrado abaixo
class A:
	# Aqui, vai printar o valor da variável 'a' definida no escopo global
	# Caso definíssemos uma variável com mesmo nome e valor diferente dentro da classe, ela sobrescreveria a variável
	# que está no escopo global
	print(a)
	print(globals())
	# Aqui serão printadas as propriedades que são de escopo local: o módulo ao qual a classe pertence e o
	# qualificador (nome) da classe
	print(locals())


f()
