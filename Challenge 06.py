class Computador:
    def __init__(self, modelo, fabricante, processador, ram, tamanho_hd, espaço_ocupado_hd, ligado):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.ram = ram
        self.tamanho_hd = tamanho_hd
        self.espaço_ocupado_hd = espaço_ocupado_hd
        self.ligado = ligado

    def liga(self):
        if self.ligado == 1:
            return True

    def desliga(self):
        if self.ligado == 0:
            return False

    def limparHD(self, valor):
        if self.espaço_ocupado_hd - valor < 0:
            print('O valor informado é maior que o valor contido dentro do HD. Portanto ficará em 0GB!')
            self.espaço_ocupado_hd = self.espaço_ocupado_hd - self.espaço_ocupado_hd
        else:
            self.espaço_ocupado_hd = self.espaço_ocupado_hd - valor

    def ocuparHD(self, valor):
        if self.espaço_ocupado_hd + valor > self.tamanho_hd:
            print(f'Espaço disponível no HD insuficiente')
        else:
            self.espaço_ocupado_hd = self.espaço_ocupado_hd + valor

config1 = Computador('gt-254', 'Asus', 'i7 - 12700k', '32gb', 500, 150, 1)

print(f'Modelo: {config1.modelo}; Fabricante: {config1.fabricante}; Processador: {config1.processador}; Memória RAM: {config1.ram}; Tamanho do HD: {config1.tamanho_hd}; Espaço ocupado pelo HD: {config1.espaço_ocupado_hd}; Está Ligado? {config1.ligado}')

print(f'O computador está ligado? {config1.liga()}')
config1.limparHD(int(input('Deseja liberar o espaço do HD em quantos GB? ')))
config1.ocuparHD(int(input('Deseja ocupar o espaço do HD em quantos GB? ')))
print(f'Espaço ocupado do hd: {config1.espaço_ocupado_hd}GB')
