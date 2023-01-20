"""
>>> def ola():
...    print('Olá')
...
>>> executar(ola)
Olá
>>> executar(ola, 2)
Olá
Olá
>>> def ola_mundo():
...    print('Olá Mundo')
>>> executar(ola_mundo, 3)
Olá Mundo
Olá Mundo
Olá Mundo
"""


def executar(f, n=1):
	for _ in range(n):
		f()


# Uma função que pode receber outras funções como argumento e na qual essas funções são executadas internamente é
# chamada de função de alta ordem
# Qualquer função pode ser passada como argumento
