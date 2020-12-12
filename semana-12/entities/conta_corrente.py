from entities.conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_da_conta: int, saldo: float, taxa_de_operacao):
        super().__init__(numero_da_conta, saldo)
        self.__taxa_de_operacao = taxa_de_operacao

    def sacar(self, valor_de_saque: float):
        if(self.__check_saque(valor_de_saque)):
            self.saldo = (self.saldo - valor_de_saque) - self.__valor_da_taxa_de_operacao(valor_de_saque)
        else:
            print("Não foi possível realizar esta operação")

    def depositar(self, deposito: float):
        self.saldo = (self.saldo + deposito) - self.__valor_da_taxa_de_operacao(deposito)

    def __valor_da_taxa_de_operacao(self, valor_saque_ou_deposito: float):
        return valor_saque_ou_deposito * (self.__taxa_de_operacao / 100)

    def __check_saque(self, valor_de_saque):
        if((self.saldo - valor_de_saque) - self.__valor_da_taxa_de_operacao(valor_de_saque) >= 0):
            return True
        else:
            return False

    def __str__(self):
        return f"Numero da conta: {self.numero_da_conta} - " \
               f"Valor do saldo: {self.saldo}"