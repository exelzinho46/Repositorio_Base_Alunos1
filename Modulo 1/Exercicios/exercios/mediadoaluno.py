nome = input("digite o seu nome:")
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota:"))
media = nota = (nota1+ nota2 + nota3) / 3

if media >= 7:
    print("voce foi aprovado!")
elif media >= 5:
    print("voce esta de recuperaçao")
else:
    print("voce esta reprovado!")
    


