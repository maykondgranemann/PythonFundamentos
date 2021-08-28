# Crie um cadastro de clientes para uma loja de bebidas
# O cadastro deve solicitar ao usuário:
# Nome, Sobrenome e idade
# O sistema deve permitir apenas clientes maiores de idade
# Caso a idade seja menor, informar que nao pode ser cadastrado


print('*'*10, 'Cadastro de Clientes', '*'*10)
print('\n')
nome = input('Digite o seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))

if(idade >= 18):
    print('Cadastrado com sucesso!')
elif(idade > 0):
    print('Nao permitido menores de idade')
else:
    print('Idade informada é inválida')
