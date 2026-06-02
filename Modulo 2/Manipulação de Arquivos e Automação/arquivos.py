import csv


with open('dados.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)


    for linha in leitor_csv:
        nome,idade,nota = linha
        print(f"{nome:^15} | {idade:^10} | {nota:^10}")
