nomeAtleta = ' '

while (nomeAtleta != ''):
    nomeAtleta = input('Atleta: ')

    if (nomeAtleta != ''):
        primeiroSalto = float(input('Primeiro Salto: '))
        segundoSalto = float(input('Segundo Salto: '))
        terceiroSalto = float(input('Terceiro Salto: '))
        quartoSalto = float(input('Quarto Salto: '))
        quintoSalto = float(input('Quinto Salto: '))

        somaSaltos = primeiroSalto + segundoSalto + \
            terceiroSalto + quartoSalto + quintoSalto
        if (primeiroSalto >= segundoSalto) and \
           (primeiroSalto >= terceiroSalto) and \
           (primeiroSalto >= quartoSalto) and \
           (primeiroSalto >= quintoSalto):
            melhorSalto = primeiroSalto
        elif (segundoSalto >= terceiroSalto) and \
             (terceiroSalto >= quartoSalto) and \
             (quartoSalto >= quintoSalto):
            melhorSalto = segundoSalto
        elif (terceiroSalto >= quartoSalto) and \
             (terceiroSalto >= quintoSalto):
            melhorSalto = terceiroSalto
        elif (quartoSalto >= quintoSalto):
            melhorSalto = quartoSalto
        else:
            melhorSalto = quintoSalto
        somaSaltos -= melhorSalto

        if (primeiroSalto <= segundoSalto) and \
           (primeiroSalto <= terceiroSalto) and \
           (primeiroSalto <= quartoSalto) and \
           (primeiroSalto <= quintoSalto):
            piorSalto = primeiroSalto
        elif (segundoSalto <= terceiroSalto) and \
             (terceiroSalto <= quartoSalto) and \
             (quartoSalto <= quintoSalto):
            piorSalto = segundoSalto
        elif (terceiroSalto <= quartoSalto) and (terceiroSalto <= quintoSalto):
            piorSalto = terceiroSalto
        elif (quartoSalto <= quintoSalto):
            piorSalto = quartoSalto
        else:
            piorSalto = quintoSalto
        somaSaltos -= piorSalto

        print('Melhor Salto: %.2f m' % (melhorSalto))
        print('Pior Salto: %.2f m' % (piorSalto))
        print('Media dos demais saltos: %.2f m' % (somaSaltos / 3.0))

        print('Resultado Final: ')
        print('%s: %.2f m' % (nomeAtleta, (somaSaltos / 3.0)))
