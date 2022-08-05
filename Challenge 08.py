class Empresa:
    def __init__(self, nome, cnpj, media_funcionarios, media_lucro_mensal):
        self.nome = nome
        self.cnpj = cnpj
        self.media_funcionarios = media_funcionarios
        self.media_lucro_mensal = media_lucro_mensal


class Prefeitura(Empresa):
    def __init__(self, nome, cnpj, media_funcionarios, media_lucro_mensal, cidade, valor_total_impostos):
        super().__init__(nome, cnpj, media_funcionarios, media_lucro_mensal)
        self.cidade = cidade
        self.prefeito = []
        self.valor_total_impostos = valor_total_impostos

    def arrecadacao(self):
        r = self.media_lucro_mensal * 0.016
        self.valor_total_impostos = r
        return self.valor_total_impostos

    def inserir_prefeitos(self, prefeito):
        self.prefeito.append(prefeito)

    def listar_prefeitos(self):
        for prefeito in self.prefeito:
            print(f'Nome do prefeito: {prefeito.nome}')
            print(f'CPF do prefeito: {prefeito.cpf}')
            print(f'Formação do prefeito: {prefeito.formacao}')

class Prefeito:
    def __init__(self, nome, cpf, formacao):
        self.nome = nome
        self.cpf = cpf
        self.formacao = formacao

prefeitura1 = Prefeitura('Soluções Tecnológicas', '23.113.536/0001-19', 10, 100000.00, 'Fortaleza', 0)
prefeitura1.arrecadacao()
prefeito1 = Prefeito('José', '354.564.321-45', 'Administração')
prefeitura1.inserir_prefeitos(prefeito1)

prefeitura2 = Prefeitura('Indutrial Ltda.', '33.135.766/0001-21', 200, 500000.00, 'Fortaleza', 0)
prefeitura2.arrecadacao()
prefeito2 = Prefeito('José', '354.564.321-45', 'Administração')
prefeitura2.inserir_prefeitos(prefeito2)

print(f'Nome da Empresa: {prefeitura1.nome}/ CNPJ: {prefeitura1.cnpj}. Lucro mensal: R${prefeitura1.media_lucro_mensal:.2f}')
print(f'Prefeitura de: {prefeitura1.cidade}')
prefeitura1.listar_prefeitos()
print(f'Valor arrecadado: R${prefeitura1.valor_total_impostos:.2f}')

print('-' * 100)

print(f'Nome da Empresa: {prefeitura2.nome}/ CNPJ: {prefeitura1.cnpj}. Lucro mensal: R${prefeitura2.media_lucro_mensal:.2f}')
print(f'Prefeitura de: {prefeitura2.cidade}')
prefeitura1.listar_prefeitos()
print(f'Valor arrecadado: R${prefeitura2.valor_total_impostos:.2f}')

print('-' * 100)

print(f'Total Arrecadado: R${prefeitura1.valor_total_impostos + prefeitura2.valor_total_impostos:.2f}')
