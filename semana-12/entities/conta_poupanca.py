from entities.conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_da_conta: int, saldo: float, limite: float):
        super().__init__(numero_da_conta, saldo)
        self.__limite = limite

    def sacar(self, valor_de_saque: float):
        if(self.__check_saque(valor_de_saque)):
            self.saldo = (self.saldo - valor_de_saque)
        else:
            print("Não foi possível realizar esta operação")

    def depositar(self, deposito: float):
        self.saldo += deposito

    def __check_saque(self, valor_de_saque: float):
        if(valor_de_saque > (self.saldo + self.__limite)):
            return False
        else:
            return True

    def __str__(self):
        return f"Numero da conta: {self.numero_da_conta} - " \
               f"Valor do saldo: {self.saldo} - " \
               f"Valor do limite: {self.__limite}"