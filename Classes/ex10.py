class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        self.setQuantidadeCombustivel(self.quantidadeCombustivel + totalLitros)

    def abastecerPorLitro(self, totalLitros):
        self.setQuantidadeCombustivel(self.quantidadeCombustivel + totalLitros)

bomba = BombaCombustivel('Gasolina Aditivada', 3.03, 100)
print('abastecendo 100 litros')
bomba.abastecerPorLitro(100)
print('Tem ', bomba.quantidadeCombustivel, ' litros')

print('abastecendo 100 pilas')
bomba.abastecerPorValor(100)
print('Tem ', bomba.quantidadeCombustivel, ' litros')
