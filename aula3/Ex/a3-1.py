# Exercicio 1 - Aula Funcoes e Procedimentos
# Crie um sistemas de cadastro de produtos
# O sistema deve ter 4 funcoes
# 1 - Imprimir um cabecalho
#   utilizar a biblioteca os para limpar a tela
# 2 - Funcao que solicita os dados do produto
#   usar as funcoes input para solicitar nome, descricao e valor
#   salvar os dados em um dicionario
#   retornar o dicionario ao final da funcao
# 3- Funcao de validacao de dados
#   deve validar se o nome do produto maior que 5 caracteres
#   validar se valor maior que zero
# 4 - Imprimir um rodapé e os dados do produto cadastrado

import os
# f1
def cabecalho():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*20,'CADASTRO DE PRODUTOS','='*20, '\n')
# f2
def cadastra():
    produto = {}
    produto['nome'] = input('Digite o nome: ')
    produto['descricao'] = input('Digite o descricao: ')
    produto['valor'] = float(input('Digite o valor: '))
    return produto
# f3
def valida(produto):
    valido = True
    # valida nome >5
    if( len(produto['nome']) < 5 ):
        print('Nome do produto invalido! Deve ser maior que 5')
        valido = False
    # valida valor >0
    if( produto['valor'] < 0 ):
        print('O valor do produto é invalido! Deve ser maior que zero')
        valido = False
    return valido
# f4
def rodape(produto):
    print('Produto cadastrado com sucesso!')
    print('\t', produto['nome'], produto['descricao'], produto['valor'])

cabecalho()
p = cadastra()
if(valida(p)):
    rodape(p)