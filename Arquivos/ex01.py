# Método para validar o IP
def validaIP(ipAddress) -> bool:
    blocos = ipAddress.split('.')
    for i in blocos:
        i = int(i)
        if i < 0 or i > 255:
            return False
    return True

# Abre o arquivo para leitura
arquivoEntrada = open('ex01_entrada.txt', 'r')

# Coloca todas as linhas em memoria
linhas = arquivoEntrada.readlines()

# Fecha o arquivo
arquivoEntrada.close()

ipsValidos = []
ipsInvalidos = []
for ip in linhas:
    if validaIP(ip):
        ipsValidos.append(ip)
    else:
        ipsInvalidos.append(ip)

# Abre o arquivo para escrita
arquivoSaida = open('ex01_saida.txt', 'w')
arquivoSaida.write('[IPs Validos]\n')
for i in range(len(ipsValidos)):
    arquivoSaida.write(ipsValidos[i])
arquivoSaida.write('\n[IPs Invalidos]\n')
for i in range(len(ipsInvalidos)):
    arquivoSaida.write(ipsInvalidos[i])

# Fecha o arquivo
arquivoSaida.close()