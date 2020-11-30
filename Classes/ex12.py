class ContaInvestimento:
    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        print('Depositando R$', valor, ' para ', self.nomeCorrentista)
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        print('Adicianado juros na conte de: ', self.nomeCorrentista)
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

conta = ContaInvestimento(100, 'Martin', 10)
conta.deposito(1000)
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
