# Curso: Python Fundamentos Proway
# Aula : Dia 2 - Parte 3
# Assunto: Dicionários
# Data: 2021-08-28

#bebidas = 

lista = ['maykon']
tuplas = ('maykon')
lista[0]
tuplas[0]

# Criando um dicionario 
dicionario = {'nome':'maykon', 'sobrenome':'granemann', 'idade':10}

# Lendo dados de um dicionario
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# Alterando dados de um dicionario
dicionario['nome'] = 'Joana'
dicionario['sobrenome'] = 'Nascimento'
dicionario['idade'] = 22

# Lendo os dados alterados
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# adicionando um novo conjunto d chave:valor
dicionario['cpf'] = '0555545646'
print(dicionario['cpf'])


cliente = {}
cliente2 = {'nome':'', 'sobrenome':'', 'idade':0}

cliente['nome'] = input('digite o nome: ')
cliente['sobrenome'] = input('digite o sobrenome: ')
cliente['idade'] = int(input('digite a idade: '))

print(cliente)
# Deletando uma chave de um dicionario
del(cliente['idade'])
print(cliente)

cliente2['nome'] = input('digite o nome: ')
cliente2['sobrenome'] = input('digite o sobrenome: ')
cliente2['idade'] = int(input('digite a idade: '))

clientes = [cliente, cliente2]
print(clientes)