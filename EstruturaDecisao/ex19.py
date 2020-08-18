num = int(input('Informe um numero inteiro: '))

centenas = num / 100
dezenas = (num - (centenas * 100)) / 10
unidades = (num - (centenas * 100) - (dezenas * 10))

result = ''
if (centenas > 0):
    result = result + str(centenas)
    if (centenas > 1):
        result = result + ' centenas '
    else:
        result = result + ' centena '

if (dezenas > 0):
    if (unidades == 0) and (centenas != 0):
        result = result + 'e '
    result = result + str(dezenas)
    if (dezenas > 1):
        result = result + ' dezenas '
    else:
        result = result + ' dezena '

if (unidades > 0):
    if (centenas != 0) or (dezenas != 0):
        result = result + 'e '
    result = result + str(unidades)
    if (unidades > 1):
        result = result + ' unidades'
    else:
        result = result + ' unidade'

print(result)
