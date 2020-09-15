for i in range(0, 10):
    codigo = int(input('Informe o numero do aluno: '))
    altura = int(input('Informe a altura do aluno: '))
    if ('maisAlto' not in vars()) or (altura > maisAlto):
        maisAlto = altura
        codigoMaisAlto = codigo
    if ('maisBaixo' not in vars()) or (altura < maisBaixo):
        maisBaixo = altura
        codigoMaisBaixo = codigo

print('O aluno mais alto é o de codigo %i com %f' %\
    (codigoMaisAlto, maisAlto))
print('O aluno mais baixo é o de codigo %i com %f' %\
    (codigoMaisBaixo, maisBaixo))
