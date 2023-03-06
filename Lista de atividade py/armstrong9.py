numero = int(input("Digite um número inteiro: "))

digitos = [int(d) for d in str(numero)]

soma = sum([d**3 for d in digitos])

if soma == numero:
    print(f"{numero} é um número de Armstrong")
else:
    print(f"{numero} não é um número de Armstrong")