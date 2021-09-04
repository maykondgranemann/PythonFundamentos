# Exercicio Aula2 - 3 - Dicionários
# Crie um sistema de cadastro de Produtos
# O sistema deve solicitar ao usuário que informe os seguintes dados:
#  - Nome
#  - Descrição
#  - Categoria
#  - Valor
# O sistema deve atender as seguintes regras:
#  - Permitir cadastrar produtos com valores maiores que zero
#  - O nome do produto deve ter mais de 3 letras
#  - A categoria deve possuir mais de 5 caracteres
#  - Todos os dados devem estar armazenados em um dicionario

# Exemplo de como pegar a quantidade de letras de uma variável
#   nome = 'Cerveja Skol'
#   len(nome)
import os
os.system('cls' if os.name == 'nt' else 'clear')  

print('\n', '='*15, ' Sistema de Cadastro de Produtos ', '='*15, '\n')
valido = False
prod = {}
while(not valido):
    nome = input('Digite o nome do produto: ')
    if(not len(nome) > 3 ):
        print('O nome deve ter mais que 3 caracteres!')
        input('Digite enter para continuar ...')
        # if ternario no Python, se for == 'nt'(windows) executa cls senao clear
        os.system('cls' if os.name == 'nt' else 'clear')                
    else:
        valido = True    
        prod['nome'] = nome

prod['desc'] = input('Digite a descrição do produto: ')

valido = False # atribuindo novo valor para realizar outra validação
while(not valido):
    cat = input('Digite a categoria do produto: ')
    if(not len(cat) > 5 ):
        input('A categoria deve ter mais que 5 caracteres!\nDigite enter para continuar ...')
        # if ternario no Python, se for == 'nt'(windows) executa cls senao clear
        os.system('cls' if os.name == 'nt' else 'clear')                
    else:
        valido = True    
        prod['cat'] = cat

valido = False
while(not valido):
    valor = float(input('Digite o valor do produto: '))
    if(not valor > 0 ):
        print('O valor deve ser maior que zero!')
        input('Digite enter para continuar ...')
        # if ternario no Python, se for == 'nt'(windows) executa cls senao clear
        os.system('cls' if os.name == 'nt' else 'clear')                
    else:
        valido = True    
        prod['valor'] = valor

print(prod)