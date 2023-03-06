numero = input("\nDigite um número inteiro de três dígitos: ")

if len(numero) != 3:
    print("\nNúmero inválido")
else:
    soma_digitos = int(numero[0]) + int(numero[1]) + int(numero[2])

    print("\nA soma dos dígitos é:", soma_digitos)