nome = input("Digite o seu nome:")
idade = int(input("digite a sua idade:"))
possui_carteira_motorista =  input("possui carteira de motorista? \n (1-sim) (2-não)")
if idade >= 18:
    if possui_carteira_motorista == "1":
        print("pode dirigir.")
    else:
        print("Você não pode dirigir.")
else:
    print("menor de idade")

