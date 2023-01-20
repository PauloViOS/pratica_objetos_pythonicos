# Isso nos traz os nomes de todas as funções presentes no namespace 'global' dentro da aplicação
print(globals())

# a declaração de uma variável ou função da forma como é feita abaixo, faz com que o "escopo" dela seja apenas o
# módulo em que foi declarada (o que, para o Python, é global). Se fizermos print(globals()) após a declaração da
# variável 'a' abaixo, veremos que ela aparecerá no print
a = 5
print(globals())


def foo():
	pass
