# Crie um sistema para cadastro de pessoa
# o sistema deve pedir o nome, idade e sexo
# cada dado deve ser armazenado em uma variável
# ao final, o programa deve imprimir uma frase com os dados do usuario

print('='*10,'Sistema de cadastro de pessoas','='*10)
print('\n')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('Digite seu sexo: ')
print('\n')
print('Pessoa cadastrada com sucesso!\n', nome, idade, sexo)
