# Curso: Python Fundamentos Proway
# Aula : Dia 4 - Parte 4 - 1
# Assunto: Criando Arquivos - W
# Data: 2021-09-11

# Primeiro argumento é o nome do arquivo, 
#  o nome pode ter o caminho da pasta
# Segundo arquivo é o tipo de abertura
# 'w' - se o arquivo nao existir, cria. 
#   Caso exista, sobreescreve
arquivo = open('aula4\cliente.txt', 'w')
arquivo.write('Cliente1-ClientePF')
arquivo.close()