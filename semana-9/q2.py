'''
2.Modele uma classe funcionário.Ela deve ter o nome do funcionário, o departamento onde o mesmo trabalha,
seu salário (float), a data de entrada no banco (str) e seu RG (str).

Você deve criar alguns métodos de acordo com sua necessidade.

Além deles, crie um método receberAumento(percentual_aumento: str) que aumenta o salário do funcionário
de acordo com o parâmetro passado como argumento. 

Crie também um método chamado calcular_ganho_anual, que não recebe parâmetro algum,
devolvendo o valor do salário multiplicado por 12. Por fim, crie uma aplicação teste para verificar sua classe.
'''

from funcionario import Funcionario

def main():
    funcionario = Funcionario("yudi", "banco imobiliário", 8001, "12/12/2012", "4002.8922")
    funcionario.mostrar_dados_do_funcionario()
    funcionario.mostrar_ganho_anual()
    funcionario.receber_aumento(10)
    funcionario.mostrar_dados_do_funcionario()
main()