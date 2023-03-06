num = int(input("\nDigite um número: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("O número não é primo")
            break
    else:
        print("O número é primo")
else:
    print("O número não é primo")