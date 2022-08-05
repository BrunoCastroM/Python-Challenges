class Pessoas:
    def __init__(self, nome, idade, endereco, afinidade):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.afinidade = afinidade
# Se a afinidade for 0 = Familia; se 1 = Amigos; e se for 3 = Guia


class Trilha(Pessoas):
    contador = 0
    def __init__(self, nome, idade, endereco, afinidade, distancia, dificuldade, localizacao):
        super().__init__(nome, idade, endereco, afinidade)
        self.distancia = distancia
        self.dificuldade = dificuldade
        self.localizacao = localizacao
        self.pontuacao = 0
        self.valor_medio_trilha = 0

    def gameficacao(self):
        Trilha.contador += 1
        if Trilha.contador > 10:
            self.pontuacao -= 5
        if self.afinidade == 0:
            self.pontuacao += 20
            if self.idade < 18:
                self.pontuacao += 10
                return self.pontuacao
        elif self.afinidade == 1:
            self.pontuacao += 15
            if self.idade < 18:
                self.pontuacao += 10
                return self.pontuacao
        elif self.afinidade == 2:
            self.pontuacao -= 5
            return self.pontuacao

    def valor_trilha(self):
        if self.afinidade == 2:
            self.valor_medio_trilha += 150


trilha1 = Trilha('Zé', 17, 'Rua da Feira, 25', 0, 20, 'Fácil', 'Vale do Capão')
trilha1.gameficacao()

trilha2 = Trilha('João', 50, 'Rua da Feira, 25', 0, 20, 'Fácil', 'Vale do Capão')
trilha2.gameficacao()

trilha3 = Trilha('Ana', 47, 'Rua da Feira, 25', 0, 20, 'Fácil', 'Vale do Capão')
trilha3.gameficacao()

trilha4 = Trilha('Rafael', 15, 'Rua José Figueredo, 321', 1, 20, 'Fácil', 'Vale do Capão')
trilha4.gameficacao()

trilha5 = Trilha('Marcos', 32, 'Av. Doutor Lira, 0764', 1, 20, 'Fácil', 'Vale do Capão')
trilha5.gameficacao()

trilha6 = Trilha('Josefina', 33, 'Av. Doutor Lira, 0764', 1, 20, 'Fácil', 'Vale do Capão')
trilha6.gameficacao()

trilha7 = Trilha('Natalhia', 22, 'Rua Sargento Manuel, 90', 1, 20, 'Fácil', 'Vale do Capão')
trilha7.gameficacao()

trilha8 = Trilha('Geovani', 25, 'Rua Sargento Manuel, 90', 1, 20, 'Fácil', 'Vale do Capão')
trilha8.gameficacao()

trilha9 = Trilha('Anastácia', 35, 'Rua Das Flores, 12', 1, 20, 'Fácil', 'Vale do Capão')
trilha9.gameficacao()

trilha10 = Trilha('Julio', 42, 'Rua Eng. Afonso, 376', 1, 20, 'Fácil', 'Vale do Capão')
trilha10.gameficacao()

trilha11 = Trilha('Pedro', 35, 'Rua Argentina, 8596', 2, 20, 'Fácil', 'Vale do Capão')
trilha11.gameficacao()
trilha11.valor_trilha()

print(f'Mallu atingiu: {trilha1.pontuacao + trilha2.pontuacao + trilha3.pontuacao + trilha4.pontuacao + trilha5.pontuacao + trilha6.pontuacao + trilha7.pontuacao+ trilha8.pontuacao + trilha9.pontuacao + trilha10.pontuacao + trilha11.pontuacao} pontos ao todo')
print(f'Foram ao todo {trilha1.contador} pessoas na trilha do Vale do Capão')
print(f'O guia cobrou por essa trilha R${trilha11.valor_medio_trilha:.2f}')
print('-' * 55)
print(f'Nome: {trilha1.nome}\nIdade: {trilha1.idade}\nEndereço: {trilha1.endereco}\nRelação com Mallu: {trilha1.afinidade} (Família)\nDistância da trilha: {trilha1.distancia}Km\nDificuldade da trilha: {trilha1.dificuldade}\nDificuldade da trilha: {trilha1.localizacao}')
print('-' * 55)
print(f'Nome: {trilha7.nome}\nIdade: {trilha7.idade}\nEndereço: {trilha7.endereco}\nRelação com Mallu: {trilha7.afinidade} (Amiga)\nDistância da trilha: {trilha7.distancia}Km\nDificuldade da trilha: {trilha7.dificuldade}\nDificuldade da trilha: {trilha7.localizacao}')
print('-' * 55)
print(f'Nome: {trilha11.nome}\nIdade: {trilha11.idade}\nEndereço: {trilha11.endereco}\nRelação com Mallu: {trilha11.afinidade} (Guia)\nDistância da trilha: {trilha11.distancia}Km\nDificuldade da trilha: {trilha11.dificuldade}\nDificuldade da trilha: {trilha11.localizacao}')
