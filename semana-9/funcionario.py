class Funcionario:
    def __init__(self, nome:str, departamento:str, salario:float, data_de_entrada_no_banco:str, rg:str):
        self.nome = nome
        self.departamento = departamento
        self.__salario = salario
        self.data_de_entrada_no_banco = data_de_entrada_no_banco
        self.__rg = rg

    def mostrar_dados_do_funcionario(self):
        print(f'''
        Nome: {self.nome}
        Departamento: {self.departamento}
        Salario: {self.__salario}
        Data de entrada no banco: {self.data_de_entrada_no_banco}
        rg: {self.__rg}
        ''')

    def __calcular_ganho_anual(self):
        ganho_anual = self.__salario * 12
        return ganho_anual
    
    def receber_aumento(self, percentual_de_aumento: float):
        aumento = (self.__salario * percentual_de_aumento) / 100
        self.__salario += aumento
    
    def mostrar_ganho_anual(self):
        print(f'Ganho anual do funcionário: {self.__calcular_ganho_anual()}')