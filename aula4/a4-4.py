# Curso: Python Fundamentos Proway
# Aula : Dia 4 - Parte 4 - 4
# Assunto: Criando Arquivos - R
# Data: 2021-09-11



arquivo = open('aula4\categoria.txt', 'r')
# ReadLines = cria uma lista de string com todas as linhas do arquivo
linhas = arquivo.readlines()

for l in  linhas :
    l_sem_barra_n = l.strip() # Strip remove \n, \t e espacos em branco
    print(l_sem_barra_n)

# Fechando o arquivo
arquivo.close()