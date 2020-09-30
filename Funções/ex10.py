import random
import time
def lancamento_dados():
    resultado_lancamento = random.randrange(2, 13)
    return resultado_lancamento
def verificar_resultado(lancamento):
    if lancamento in [7, 11]:
        print("Você tirou: ", lancamento, "\nVocê é um natural e ganhou!")
    elif lancamento in [2, 3, 12]:
        print("Você tirou: ", lancamento, "\n[Craps] VOCÊ PERDEU!")
    else:
        print("Você tirou: ", lancamento, "\nVocê ganhou um Ponto")
        numero_tirado = lancamento
        lancamento2 = True
        while numero_tirado != lancamento2:
            lancamento2 = random.randrange(2, 13)
            if lancamento2 == 7:
                print("Você tirou: ", lancamento2, "\nVocê perdeu!")
                break
            elif lancamento2 == numero_tirado:
                print("Você tirou: ", lancamento2, "\nVocê tirou o mesmo número novamente. você GANHOU")
            else:
                print("Você tirou:", lancamento2, "\nJogando novamente em 2 segundos...")
                time.sleep(2)
lancamento = lancamento_dados()
verificar_resultado(lancamento)