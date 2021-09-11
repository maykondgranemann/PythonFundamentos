# Curso: Python Fundamentos Proway
# Aula : Dia 4 - Parte 4 - 4
# Assunto: Criando Arquivos - A
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, 
#  o nome pode ter o caminho da pasta
# Segundo arquivo é o tipo de abertura
# 'a' - se o arquivo nao existir, cria. 
#   Caso exista, adiciona o conteudo no final do arquivo
arquivo = open('aula4\categoria.txt', 'a')
arquivo.write('Categoria 1\n') # Utiliza \n para pular de linha
arquivo.close()