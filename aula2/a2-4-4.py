# Curso: Python Fundamentos Proway
# Aula : Dia 2 - Parte 4 - 4
# Assunto: for com listas e dicionarios
# Data: 2021-09-04

produto = { 'nome':'cerveja', 'desc':'larger', 'cat':'bebida', 'valor':1.89 }
produto2 = { 'nome':'vodca', 'desc':'500ml', 'cat':'bebida', 'valor':18.99 }
produtos_lista = [produto, produto2]

# imprimindo cada dicionario
for p in produtos_lista:
    print(p)

print('\n')
# imprimindo cada chave e valor dos dicionarios de dentro da lista
for p in produtos_lista:
    for (c,v) in p.items():
        print(c,v)
    print('\n')

print('\n')
nomes = [ ['Ana', 'Paulo'], ['Silva', 'Souza'] ] 
for n in nomes:
    for s in n:
        print(s)
