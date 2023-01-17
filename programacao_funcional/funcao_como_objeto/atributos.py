def dobro(x):
	return x*2

# se abrirmos o python console e executarmos
# for p in dir(dobro):
# 	print(p)
# Veremos todas as propriedades da função, como __name__ e __module__
# Vamos dar atenção à propriedade code (dobro.__code__) que é um objeto que contém propriedades sobre o código
# presente na função. Dentro dele, temos uma propriedade co_code (dobro.__code__.co_code), que nos exibe uma
# cadeia de bytes. É essa cadeia que é gerada na compilação pela VM do Python.
# Para termos uma noção do que essa cadeia de bytes diz, vamos importar a função dis da biblioteca built-in dis (que
# vem de 'disassembler') e usar essa função no output do co_code
# dis(dobro.__code__.co_code)
# isso nos mostra as operações que a função executa

# os objetos são dinâmicos em python.
# se tentarmos acessar o atributo n da função dobro (dobro.n), vamos tomar um AttributeError, pois ele não existe.
#Podemos então, CRIAR esse atributo, atribuindo um valor a ele (dobro.n=42, por exemplo). A partir desse momento,
# ele estará acessível.
# Podemos também deletar esse atributo (del dobro.n)

# Também podemos fazer uma atribuição com funções, como com qualquer outro objeto.
# ao fazer g = dobro (sem os parênteses, pois não estamos executando a função) e executar g no console, teremos como
# retorno <function dobro at ...>, mostrando que g tem como valor a função dobro. Para comprovar isso de outra forma,
# podemos fazer g.__name__, o que retornará 'dobro'