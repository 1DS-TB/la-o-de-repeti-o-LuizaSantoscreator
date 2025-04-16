num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("Por favor, digite um número inteiro **positivo**.")
else:
    fatorial = 1
    print(f"{num}! = ", end="")

    for i in range(num, 0, -1):
        fatorial *= i
        print(i, end=" x " if i != 1 else " = ")

    print(fatorial)
