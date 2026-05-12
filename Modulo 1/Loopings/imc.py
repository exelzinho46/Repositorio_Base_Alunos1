peso = float(input("digite o seu peso: "))
altura = float(input("digite a sua altura:  "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
    print("cuidado com a saúde")
elif imc < 35:
    print("obesidade grau 1")
elif imc < 40:
    print("obesidade grau 2")
else:    print("obesidade grau 3")

