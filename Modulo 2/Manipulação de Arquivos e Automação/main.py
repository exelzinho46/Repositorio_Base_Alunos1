import csv
import os

def limpar_tela():
    os.system("cls")  
    
print("Seja bem-vindo ao sistema de notas 🧑‍🏫🤖")

while True:
    opcao = input(
        "\n== MENU ==\n"
        "[1] - cadastrar aluno e nota\n"
        "[2] - listar alunos\n"
        "[3] - listar alunos com nota acima de 8\n"
        "[0] - sair\n"
        "Sua opção: "
    )

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        idade = int(input("Digite a idade do aluno: "))
        with open('dados.csv', 'a', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow([nome, nota, idade])
            
    elif opcao == "2":
        print("Listar alunos")

    elif opcao == "3":
        print("Listar alunos com nota acima de 8")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

    input("\nAperte ENTER para continuar...")
    limpar_tela()

