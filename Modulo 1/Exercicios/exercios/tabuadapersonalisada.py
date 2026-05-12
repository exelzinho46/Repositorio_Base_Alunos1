numero = int(input("digite um numero da tabuada: "))
inicio = int(input("digite de onde a tabuada deve começar: "))
fim = int(input("digite onde a tabuada deve terminar: "))
for i  in range(inicio, fim + 1):
    print(f"{i} x {numero} = {i * numero}")
    