
#with open("teste.txt", "w",encoding="utf-8") as abacaxi:
#    abacaxi.write("Não precisa colocar o .close()")

with open('teste.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for l in  linhas :
        l_sem_barra_n = l.strip() # Strip remove \n, \t e espacos em branco
        print(l_sem_barra_n)
