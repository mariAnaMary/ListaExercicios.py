Nome = input("Informe seu nome: ")
Idade = int(input("Informe sua idade: "))

if Idade <18:
    print(Nome+", você é menor de idade")

elif Idade > 18:
    print(Nome+", você é adulto")

elif Idade > 65:
    print(Nome+", você é Idoso")