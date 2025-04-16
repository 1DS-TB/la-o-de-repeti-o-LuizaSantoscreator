numeros = int(input('Informe um número: '))

if numeros <=1:
    print('O número não é primo')
else:

    for numero in range(2, numeros):
        if numeros % numero == 0:
            print('O número não é primo.')
            break
    else:
        print('O número é primo')
