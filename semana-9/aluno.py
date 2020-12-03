class Aluno:
    def __init__(self, nome:str, matricula:int, endereco:str, cpf:str):
        self.nome = nome
        self.__matricula = matricula
        self.endereco  = endereco
        self.__cpf = cpf
    def mostrar_dados_do_aluno(self):
        print('''
        Nome: {self.nome}
        Matrícula: {self.__matricula}
        Endereço: {self.endereco}
        CPF: {self.__cpf}
        ''')