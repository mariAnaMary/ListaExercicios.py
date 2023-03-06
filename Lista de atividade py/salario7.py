nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500.0:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento
diferenca = novo_salario - salario

# exibe o novo salário e a diferença
print(f"Novo salário de {nome}: R$ {novo_salario:.2f}")
print(f"Diferença entre o salário antigo e o novo: R$ {diferenca:.2f}")