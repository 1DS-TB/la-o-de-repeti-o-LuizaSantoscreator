N = int(input('Informe um valor: '))

for i in range(1, N + 1):
    for _ in range(i):
        print("*", end="")
    print()
