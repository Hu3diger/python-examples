numero = 0
while (numero <= 0):
    numero = int(input('Voce quer ver se qual numero é primo: '))
    if (numero <= 0):
        print('O numero deve ser positivo!')

primo = True
for i in range(2, numero / 2 + 1):
    if (numero % i == 0):
        primo = False
        break

if (primo):
    print('O numero é primo')
else:
    print('O numero nao é primo')
    print('Ele é divisivel por',)
    for i in range(1, numero + 1):
        if (numero % i == 0):
            print(i),
