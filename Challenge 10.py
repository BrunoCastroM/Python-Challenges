from abc import ABC, abstractmethod


class Registros:
    def __init__(self, nome_campeonato, nivel, local, premiacao, patrocinador_nome, patrocinador_valor, atleta_nome,
                 atleta_idade, atleta_pontuacao, atleta_categoria, vencedor):
        self.nome_campeonato = nome_campeonato
        self.nivel = nivel
        self.local = local
        self.premiacao = premiacao
        self.patrocinador_nome = patrocinador_nome
        self.patrocinador_valor = patrocinador_valor
        self.atleta_nome = atleta_nome
        self.atleta_idade = atleta_idade
        self.atleta_pontuacao = atleta_pontuacao
        self.atleta_categoria = atleta_categoria
        self.vencedor = vencedor

    # categoria 0 = amador, categoria 1 = profissional, categoria 2 = lenda / Mesma numeração para o nivel do campeonato.

    @abstractmethod
    def inscricao(self):
        pass


class Campeonato(Registros):
    def __init__(self, nome_campeonato, nivel, local, premiacao, patrocinador_nome, patrocinador_valor, atleta_nome,
                 atleta_idade, atleta_pontuacao, atleta_categoria, vencedor):
        super().__init__(nome_campeonato, nivel, local, premiacao, patrocinador_nome, patrocinador_valor, atleta_nome,
                         atleta_idade, atleta_pontuacao, atleta_categoria, vencedor)

    def inscricao(self):
        if self.atleta_categoria == 0 and self.nivel == 0:
            print(f'Parabéns {self.atleta_nome} você foi inscrito na competição amadora!')
            if self.vencedor == True:
                print('Você ganhou!!!')
                if self.nivel == 0:
                    self.atleta_pontuacao += 10
                    return self.atleta_pontuacao
                elif self.nivel == 1:
                    self.atleta_pontuacao += 50
                    return self.atleta_pontuacao
                elif self.nivel == 2:
                    self.atleta_pontuacao += 100
                    return self.atleta_pontuacao
            else:
                print('Infelizmente você não ganhou a competição e por isso não pontuou')
        elif self.atleta_categoria == 1 and self.nivel == 0:
            print(f'Parabéns {self.atleta_nome} você foi inscrito na competição amadora!')
            if self.vencedor == True:
                print('Você ganhou!!!')
                if self.nivel == 0:
                    self.atleta_pontuacao += 10
                    return self.atleta_pontuacao
                elif self.nivel == 1:
                    self.atleta_pontuacao += 50
                    return self.atleta_pontuacao
                elif self.nivel == 2:
                    self.atleta_pontuacao += 100
                    return self.atleta_pontuacao
            else:
                print('Infelizmente você não ganhou a competição e por isso não pontuou')
        elif self.atleta_categoria == 1 and self.nivel == 1:
            print(f'Parabéns {self.atleta_nome} você foi inscrito na competição profissional!')
            if self.vencedor == True:
                print('Você ganhou!!!')
                if self.nivel == 0:
                    self.atleta_pontuacao += 10
                    return self.atleta_pontuacao
                elif self.nivel == 1:
                    self.atleta_pontuacao += 50
                    return self.atleta_pontuacao
                elif self.nivel == 2:
                    self.atleta_pontuacao += 100
                    return self.atleta_pontuacao
            else:
                print('Infelizmente você não ganhou a competição e por isso não pontuou')
        elif self.atleta_categoria == 2 and self.nivel == 0:
            print(f'Parabéns {self.atleta_nome} você foi inscrito na competição amadora!')
            if self.vencedor == True:
                print('Você ganhou!!!')
                if self.nivel == 0:
                    self.atleta_pontuacao += 10
                    return self.atleta_pontuacao
                elif self.nivel == 1:
                    self.atleta_pontuacao += 50
                    return self.atleta_pontuacao
                elif self.nivel == 2:
                    self.atleta_pontuacao += 100
                    return self.atleta_pontuacao
            else:
                print('Infelizmente você não ganhou a competição e por isso não pontuou')
        elif self.atleta_categoria == 2 and self.nivel == 1:
            print(f'Parabéns {self.atleta_nome} você foi inscrito na competição profissional!')
            if self.vencedor == True:
                print('Você ganhou!!!')
                if self.nivel == 0:
                    self.atleta_pontuacao += 10
                    return self.atleta_pontuacao
                elif self.nivel == 1:
                    self.atleta_pontuacao += 50
                    return self.atleta_pontuacao
                elif self.nivel == 2:
                    self.atleta_pontuacao += 100
                    return self.atleta_pontuacao
            else:
                print('Infelizmente você não ganhou a competição e por isso não pontuou')
        elif self.atleta_categoria == 2 and self.nivel == 2:
            print(f'Parabéns {self.atleta_nome} você foi inscrito na competição lenda!')
            if self.vencedor == True:
                print('Você ganhou!!!')
                if self.nivel == 0:
                    self.atleta_pontuacao += 10
                    return self.atleta_pontuacao
                elif self.nivel == 1:
                    self.atleta_pontuacao += 50
                    return self.atleta_pontuacao
                elif self.nivel == 2:
                    self.atleta_pontuacao += 100
                    return self.atleta_pontuacao
            else:
                print('Infelizmente você não ganhou a competição e por isso não pontuou')
        else:
            print(f'Não foi possível fazer sua inscrição {self.atleta_nome}, a sua categoria não condiz com o nivel do campaonato')


atleta1 = Campeonato('Liga Brasileira de Tênis de Mesa', 0, 'Rua Nazaré, 1609', 2000, 'Rogério das Padarias', 500,
                     'Juliano', 19, 0, 1, False)
atleta1.inscricao()
print(f'Você está com {atleta1.atleta_pontuacao} pontos')

print('-' * 100)

atleta2 = Campeonato('Liga Brasileira de Tênis de Mesa', 1, 'Rua Nazaré, 1609', 5000, 'Fernando das Padarias', 2000,
                     'Pedro', 22, 0, 1, True)
atleta2.inscricao()
print(f'Você está com {atleta2.atleta_pontuacao} pontos')

print('-' * 100)

atleta3 = Campeonato('Liga Brasileira de Tênis de Mesa', 2, 'Rua Pardal, 1609', 7500, 'Julio da Construção', 3000,
                     'Roberta', 23, 0, 0, True)
atleta3.inscricao()
print(f'Você está com {atleta3.atleta_pontuacao} pontos')
