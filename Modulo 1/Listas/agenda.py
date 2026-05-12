import os

def limpa_tela():
    os.system("cls")
   
def adicionar_nome(listas_nomes, nome):
    listas_nomes.append(nome) #adicionar nome da listas_nomes
    
def remover_nomes(listas_nomes, nome):
    listas_nomes.remove(nome)
     
def mostrar_nomes(listas_nomes):
    for nome in listas_nomes:
        print(nome)
limpa_tela()
nomes = []


while True:
    limpa_tela()
    menu = input("Escolha sua opçao: \n[1 - listar nome\n[2] adicionar nome\n[3] remover nome\nSua opçao: ")
    if menu =="0":
        break
    elif menu == "1":
        mostrar_nomes(nomes)
        input("apertar enter e continuar")
    elif menu == "2":
        nome_salvar = input("Digite o nome que deseja adicionar: ")
        adicionar_nome(nomes, nome_salvar)
    elif menu == "3":
        nome_remover = input("digite o nome que deseja remover: ")
        remover_nomes(nomes, nome_remover)
    elif menu == "4":
        nome_procurado = input("Digite o nome que deseja procurar: ").strip()
    
    else:
        print("opçao invalida. ")
        input("Aperte enter para continuar")
   