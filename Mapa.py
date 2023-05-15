from Adjacente import Adjacente
from Estacao import Estacao

class Mapa:
    
    def __init__(self, estacao_final):
        self.estacao_final = estacao_final-1
        
    def estacoesAdjacentes(self, estacao01, estacao02, valor):
        estacao01.addEstacaoAdjacente(Adjacente(estacao02, valor))
        estacao02.addEstacaoAdjacente(Adjacente(estacao01, valor))

    def criarMapa(self):
    
        matriz_estacoes = [
        (0,    10,   18.0, 24.8, 36.4, 38.8,  35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8),# E1
        (10,   0,    8.5,  14.8, 26.2, 29.1,  26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8),# E2
        (18.0, 8.5,  0,    6.3,  18.2, 20.6,  17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6),# E3
        (24.8, 14.8, 6.3,  0,    12,   14.4,  11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4),# E4
        (36.4, 26.6, 18.2, 12,   0,    3,     2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9),# E5
        (38.8, 29.1, 20.6, 14.4, 3,    0,     3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2),# E6
        (35.8, 26.1, 17.6, 11.5, 2.4,  3.3,   0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6),# E7
        (25.4, 17.3, 13.6, 12.5, 19.4,   22.3,  20,   0,  8.2,  20.3, 16.1, 6.4,  22.7, 27.6),# E8
        (17.6, 10,   9.4,  12.6, 23.3, 25.7,  23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6),# E9
        (9.1,  3.5,  10.3, 16.7, 28.2, 30.3,  27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2),# E10
        (16.7, 15.5, 19.5, 23.6, 34.2, 36.7,  34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5),# E11
        (27.3, 20.9, 19.1, 18.6, 24.8, 27.6,  25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6),# E12
        (27.6, 19.1, 12.1, 10.6, 14.5, 15.2,  12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1), # E13
        (29.8, 21.8, 16.6, 15.4, 17.9, 18.2,  15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0)    # E14
        ]
        
        self.E1 = Estacao("E1", matriz_estacoes[self.estacao_final][0])
        self.E2 = Estacao("E2", matriz_estacoes[self.estacao_final][1])
        self.E3 = Estacao("E3", matriz_estacoes[self.estacao_final][2])
        self.E4 = Estacao("E4", matriz_estacoes[self.estacao_final][3])
        self.E5 = Estacao("E5", matriz_estacoes[self.estacao_final][4])
        self.E6 = Estacao("E6", matriz_estacoes[self.estacao_final][5])
        self.E7 = Estacao("E7", matriz_estacoes[self.estacao_final][6])
        self.E8 = Estacao("E8", matriz_estacoes[self.estacao_final][7])
        self.E9 = Estacao("E9", matriz_estacoes[self.estacao_final][8])
        self.E10 = Estacao("E10", matriz_estacoes[self.estacao_final][9])
        self.E11 = Estacao("E11", matriz_estacoes[self.estacao_final][10])
        self.E12 = Estacao("E12", matriz_estacoes[self.estacao_final][11])
        self.E13 = Estacao("E13", matriz_estacoes[self.estacao_final][12])
        self.E14 = Estacao("E14", matriz_estacoes[self.estacao_final][13])
        
        #Linha Azul
        self.estacoesAdjacentes(self.E1, self.E2, 10)
        self.estacoesAdjacentes(self.E2, self.E3, 8.5)
        self.estacoesAdjacentes(self.E3, self.E4, 6.3)
        self.estacoesAdjacentes(self.E4, self.E5, 13)
        self.estacoesAdjacentes(self.E5, self.E6, 3)
        
        #Linha Vermelha
        self.estacoesAdjacentes(self.E11, self.E9, 12.2)
        self.estacoesAdjacentes(self.E9, self.E3, 9.4)
        self.estacoesAdjacentes(self.E3, self.E13, 18.7)

        #Linha Verde
        self.estacoesAdjacentes(self.E12, self.E8, 6.4)
        self.estacoesAdjacentes(self.E8, self.E4, 15.3)
        self.estacoesAdjacentes(self.E4, self.E13, 12.8)
        self.estacoesAdjacentes(self.E13, self.E14, 5.1)

        #Linha Amarela
        self.estacoesAdjacentes(self.E10, self.E2, 3.5)
        self.estacoesAdjacentes(self.E2, self.E9, 10)
        self.estacoesAdjacentes(self.E9, self.E8, 9.6)
        self.estacoesAdjacentes(self.E8, self.E5, 30)
        self.estacoesAdjacentes(self.E5, self.E7, 2.4)
