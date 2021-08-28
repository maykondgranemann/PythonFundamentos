# Curso: Python Fundamentos Proway
# Aula : Dia 2 - Parte 2
# Assunto: Laço de repetição while, instruções aninhadas
# Data: 2021-08-28

# repeticoes = 0
# while(repeticoes <=3): #enquanto 
#     idade = input('Digite a idade: ')
#     repeticoes = repeticoes +1



# print('*'*10, 'Cadastro de Clientes', '*'*10)
# print('\n')
# nome = input('Digite o seu nome: ')
# sobrenome = input('Digite seu sobrenome: ')
# idade = int(input('Digite sua idade: '))

# invalido = True
# while(invalido):
#     if(idade >= 18):
#         print('Cadastrado com sucesso!')
#         invalido = False
#     elif(idade > 0):
#         print('Nao permitido menores de idade')
#         invalido = False
#     else:
#         print('Idade informada é inválida')
#         idade = int(input('Digite sua idade novamente: '))
import os

invalido = True
while(invalido):
    print('*'*10, 'Sistema de bebidas', '*'*10,'\n')
    print('\t1-Cadastrar uma bebida')
    print('\t2-Listar bebidas cadastradas')
    print('\t0-Sair')
    opcao = int(input('\nDigite uma opção do menu: '))

    if(opcao < 0 or opcao >2):
        print('Opção invalida!')
        input('Digite enter para continuar...')
        os.system('clear')
    else:
        invalido= False
