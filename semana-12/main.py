'''
1. Implemente uma classe abstrata Conta Bancaria que contém como atributos
o numero da conta e o saldo, e como métodos abstratos sacar e depositar que recebem um parâmetro do tipo double.
Crie as classes Conta Corrente e Conta Poupança que herdam da Conta Bancaria.
A primeira possui um atributo taxaDeOperação que é descontado sempre que um saque e um depósito são feitos.
A segunda possui um atributo limite que dá credito a mais para o correntista caso ele precise
sacar mais que o saldo. Neste caso, o saldo pode ficar negativo desde que não ultrapasse o limite.
Contudo isso não pode acontecer na classe Conta Corrente.
Teste essa classe
'''

from entities.conta_corrente import ContaCorrente
from entities.conta_poupanca import ContaPoupanca

def main():
    print('Exemplo conta corrente')
    conta = ContaCorrente(222, 10000, 10)
    print(conta)
    conta.depositar(1000)
    print(conta)
    conta.sacar(1000)
    print(conta)
    conta.sacar(2000000)

    print('-='*30)

    print('Exemplo conta poupança')
    conta_pou = ContaPoupanca(111, 10000, 1000)
    print(conta_pou)
    conta_pou.depositar(100)
    print(conta_pou)
    conta_pou.sacar(100)
    print(conta_pou)
    conta_pou.sacar(11000)
    print(conta_pou)
    conta_pou.sacar(100000000)

if __name__ == '__main__':
    main()