class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

func1 = Funcionario('Martin', 1000)
print('Nome: %s' % func1.getNome())
print('Salario: %.2f' % func1.getSalario())
