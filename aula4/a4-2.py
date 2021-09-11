# Curso: Python Fundamentos Proway
# Aula : Dia 4 - Parte 4 - 2
# Assunto: Criando Arquivos - X
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, 
#  o nome pode ter o caminho da pasta
# Segundo arquivo é o tipo de abertura
# 'x' - se o arquivo nao existir, cria. 
#   Caso exista, ocorre um erro
arquivo = open('aula4\produto.txt', 'x')
arquivo.write('Produto 1')
arquivo.close()