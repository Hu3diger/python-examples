print('Informe os valores dos lados do triangulo')
lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if (lado1 > (lado2 + lado3)) or (lado2 > (lado1 + lado3))\
        or (lado3 > (lado1 + lado2)):
    isTriangulo = False
else:
    isTriangulo = True

if (isTriangulo):
    print('Os valores formam um Triangulo do tipo: ')
    if (lado1 == lado2) and (lado2 == lado3):
        print('Equilatero')
    elif (lado1 == lado2) or (lado1 == lado2) or (lado2 == lado3):
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Os valores nao formam um Triangulo')
