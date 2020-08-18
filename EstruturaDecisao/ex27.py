totalMorangos = float(input('Informe a quantidade (em Kg) de morangos comprados: '))
totalMacas = float(input('Informe a quantidade (em Kg) de macas comprados: '))

if (totalMorangos <= 5):
    valorMorangos = totalMorangos * 2.5
else:
    valorMorangos = totalMorangos * 2.2

if (totalMacas <= 5):
    valorMacas = totalMacas * 1.8
else:
    valorMacas = totalMacas * 1.5

valorBruto = valorMorangos + valorMacas
if ((totalMorangos + totalMacas) >= 8) or (valorBruto >= 25):
    valorBruto = valorBruto * 0.9

print('Valor a pagar: ', str(valorBruto))
