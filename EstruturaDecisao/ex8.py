preco1 = int(input('Informe o primeiro preco: '))
preco2 = int(input('Informe o segundo preco: '))
preco3 = int(input('Informe o terceiro preco: '))

if (preco1 == preco2) and (preco1 == preco3):
    print('Pode comprar qualquer um, ja que os precos sao iguais.')
elif (preco1 < preco2) and (preco1 < preco3):
    print('Compre pelo primeiro preco')
elif (preco2 < preco3):
    print('Compre pelo segundo preco')
else:
    print('Compre pelo terceiro preco')
