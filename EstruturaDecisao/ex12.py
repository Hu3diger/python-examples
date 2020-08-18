valorPorHora = float(input('Informe o valor da hora trabalhada: '))
quantidadéoras = float(input('Informe a quantidade de horas trabalhadas no mes:'))

salarioBruto = valorPorHora * quantidadéoras
if (salarioBruto > 2500):
    aliquotaIR = 20
elif (salarioBruto > 1500):
    aliquotaIR = 10
elif (salarioBruto > 900):
    aliquotaIR = 5
else:
    aliquotaIR = 0

valorIR = salarioBruto * (aliquotaIR / 100.0)
valorSindicato = salarioBruto * (3 / 100.0)
totalDescontos = valorIR + valorSindicato
valorFGTS = salarioBruto * (11 / 100.0)
salarioLiquido = salarioBruto - totalDescontos

print('Salario Bruto: (' +  valorPorHora +  '*' + quantidadéoras +  '): R$' +  salarioBruto)
print('(-) IR (' +  aliquotaIR +  '%): R$' + valorIR)
print('(-) Sindicato ( 3 %): R$' + valorSindicato)
print('FGTS ( 11 %): R$' +  valorFGTS)
print('Total de Descontos: R$' + totalDescontos)
print('Salario Liquido: R$' + salarioLiquido)
