from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero_da_conta: int, saldo: float):
        self.__numero_da_conta = numero_da_conta
        self.__saldo = saldo

    @abstractmethod
    def sacar(self, valor_de_saque: float):
        pass

    @abstractmethod
    def depositar(self, deposito: float):
        pass

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_numero_da_conta(self):
        return self.__numero_da_conta

    def set_numero_da_conta(self, numero_da_conta):
        self.__numero_da_conta = numero_da_conta

    saldo = property(get_saldo, set_saldo)
    numero_da_conta = property(get_numero_da_conta, set_numero_da_conta)