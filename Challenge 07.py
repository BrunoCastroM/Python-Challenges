class Veiculos:
    def __init__(self):
        self.__tipo = ''
        self.__placa = ''
        self.__modelo = ''
        self.__dia_entrada = 0
        self.__dia_saida = 0
        self.__hora_entrada = 0
        self.__hora_saida = 0
        self.__min_entrada = 0
        self.__min_saida = 0
        self.__valor_da_hora = 0

    @property
    def tipo(self):
        return self.__tipo

    @property
    def placa(self):
        return self.__placa

    @property
    def modelo(self):
        return self.__modelo

    @property
    def dia_entrada(self):
        return self.__dia_entrada

    @property
    def dia_saida(self):
        return self.__dia_saida

    @property
    def hora_entrada(self):
        return self.__hora_entrada

    @property
    def hora_saida(self):
        return self.__hora_saida

    @property
    def min_entrada(self):
        return self.__min_entrada

    @property
    def min_saida(self):
        return self.__min_saida

    @property
    def valor_da_hora(self):
        return self.__valor_da_hora

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @dia_entrada.setter
    def dia_entrada(self, dia_entrada):
        self.__dia_entrada = dia_entrada

    @dia_saida.setter
    def dia_saida(self, dia_saida):
        if self.__dia_entrada > dia_saida:
            print('Dado inválido, o dia de entrada do veículo foi maior que o de saída')
        else:
            self.__dia_saida = dia_saida

    @hora_entrada.setter
    def hora_entrada(self, hora_entrada):
        self.__hora_entrada = hora_entrada

    @hora_saida.setter
    def hora_saida(self, hora_saida):
        if self.__hora_entrada > hora_saida:
            print('Dado inválido, o hora de entrada do veículo foi maior que o de saída')
        else:
            self.__hora_saida = hora_saida

    @min_entrada.setter
    def min_entrada(self, min_entrada):
        self.__min_entrada = min_entrada

    @min_saida.setter
    def min_saida(self, min_saida):
            self.__min_saida = min_saida

    @valor_da_hora.setter
    def valor_da_hora(self, valor_da_hora):
        self.__valor_da_hora = valor_da_hora

    def hora_total(self):
        d = self.__dia_saida - self.__dia_entrada
        d1 = d * 24
        h = self.__hora_saida - self.__hora_entrada
        if self.__min_saida > self.__min_entrada:
            m = self.__min_saida - self.__min_entrada
            m1 = m / 60
            horas_totais = d1 + h + m1
            return horas_totais
        else:
            m = self.__min_entrada - self.__min_saida
            m1 = m / 60
            horas_totais = d1 + h + m1
            return horas_totais


veiculo1 = Veiculos()
veiculo1.tipo = 'Carro'
veiculo1.placa = 'BRA2E19'
veiculo1.modelo = 'Gol'

veiculo1.dia_entrada = 1
veiculo1.hora_entrada = 8
veiculo1.min_entrada = 10

veiculo1.dia_saida = 3
veiculo1.hora_saida = 10
veiculo1.min_saida = 20

veiculo1.valor_da_hora = float(input('Digite o valor da hora: R$ '))

print(f'O veículo tipo: {veiculo1.tipo}; Placa: {veiculo1.placa}; Modelo: {veiculo1.modelo}')
print(f'Entrou dia: {veiculo1.dia_entrada}, hora: {veiculo1.hora_entrada}:{veiculo1.min_entrada}h')
print(f'Saiu dia: {veiculo1.dia_saida}, hora: {veiculo1.hora_saida}:{veiculo1.min_saida}h')
print(f'O veículo permaneceu no estacionamento: dia(s): {veiculo1.dia_saida - veiculo1.dia_entrada}, hora(s): {veiculo1.hora_saida - veiculo1.hora_entrada}:', end='')
if veiculo1.min_saida > veiculo1.min_entrada:
    print(f'{veiculo1.min_saida - veiculo1.min_entrada}h')
else:
    print(f'{veiculo1.min_entrada - veiculo1.min_saida}h')

print(f'O valor total a pagar será: R${veiculo1.hora_total() * veiculo1.valor_da_hora:.2f}')
