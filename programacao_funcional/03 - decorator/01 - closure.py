# Para entender o que são e como funcionam closures, fiz esse pequeno programa.
# O importante aqui é entender a ordem em que as coisas acontecem e porque o programa funciona
# Quando a variável 'dobro' é criada, ela guarda uma referência para a função multiplicar, que está dentro da fábrica
# de multiplicadores. Teoricamente, quando a função é executada (primeiro print), ela não deveria saber o valor do
# multiplicador que foi passado para a função fabrica_de_multiplicadores. Mas graças à closure, ela tem acesso à essa
# informação.
# Se executarmos o programa em modo debug, e colocarmos um breakpoint no "return multiplicar" e pararmos o debug
# enquanto a variávelm 'dobro' é criada, podemos inspecionar as propriedades da função multiplicar usando a função
# dir. Veremos que existe uma propriedade chamada __closure__, que é um objeto do tipo cell (olhar na doc caso não
# saiba o que é). Basicamente, esse tipo de objeto serve pra guardar variáveis que são referenciadas por múltiplos
# escopos.
# Assim, a função consegue utilizar uma variável que está disponível no escopo onde foi criada, mas não no escopo em
# que ela foi executada. Esse tipo de escopo é o chamado escopo estático, que é aquele em que não manipulamos o valor
# da variável que é exterior ao escopo da execução.
# Temos como editar o escopo estático ( o que faz com que ele não seja tão estático assim), mas isso fica pra próxima
# aula


def fabrica_de_multiplicadores(multiplicador):
	def multiplicar(n):
		return n * multiplicador

	return multiplicar


dobro = fabrica_de_multiplicadores(2)
triplo = fabrica_de_multiplicadores(3)
print(dobro(3))
print(triplo(4))

