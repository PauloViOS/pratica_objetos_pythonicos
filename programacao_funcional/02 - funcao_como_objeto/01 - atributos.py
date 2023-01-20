def dobro(x):
	return x * 2


dobro2 = lambda x: x * 2

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
# Podemos então, CRIAR esse atributo, atribuindo um valor a ele (dobro.n=42, por exemplo). A partir desse momento,
# ele estará acessível.
# Podemos também deletar esse atributo (del dobro.n)

# Também podemos fazer uma atribuição com funções, como com qualquer outro objeto.
# ao fazer g = dobro (sem os parênteses, pois não estamos executando a função) e executar g no console, teremos como
# retorno <function dobro at ...>, mostrando que g tem como valor a função dobro. Para comprovar isso de outra forma,
# podemos fazer g.__name__, o que retornará 'dobro'

# Sobre as funções anônimas
# Em termos de performance, elas são exatamente iguais às funções nomeadas, algo que pode ser comprovado ao
# executarmos um dis na função dobro2 acima.
# A diferença primordial é que a função nomeada possui um __name__ específico, enquanto qualquer função anônima irá
# retornar um mesmo valor para __name__: <lambda>.
# Isso pode fazer com que seja difícil debugar algumas coisas. Tanto é que o Luciano Ramalho recomenda não utilizar
# lambda no livro dele. Isso também é recomendado no PEP8, como podemos ver no código acima
