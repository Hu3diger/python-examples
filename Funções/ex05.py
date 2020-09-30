def somaImposto(taxaImposto, custo):
    imposto_total = custo + (custo * taxaImposto / 100)
    return imposto_total

somaImposto(27, 1000)