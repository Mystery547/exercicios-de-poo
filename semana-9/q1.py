#1.Crie uma classe Aluno com nome, matricula, endereço e cpf. Teste e exiba a informação dos alunos.
from aluno import Aluno

def main():
    aluno = Aluno("yudi", 123456, "rua bom dia e compania", "4002.8922")

    aluno.mostrar_dados_do_aluno()
main()