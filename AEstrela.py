from VetorOrdenadoAdjacente import VetorOrdenadoAdjacente

class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.fronteira = []
        self.cidadesVisitadas = []
        self.achou = False

    def buscar(self, atual):
        print('-----------------------------------')
        print('\nAtual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
        else:
            self.cidadesVisitadas.append(atual)
            print("Estações Adjacentes:\n")
            for a in atual.adjacentes:
                print('Estação: {} - F(n): {}'.format(a.estacao.nome, a.distanciaAEstrela))
                print('Fn = Gn + Hn = {} + {} = {}\n'.format(a.estacao.distanciaObjetivo, a.distancia, a.distanciaAEstrela))
                if a.estacao.visitado == False:
                    a.estacao.visitado = True
                    self.fronteira.append(a)
                else:
                    for estacoes in self.fronteira:
                        if estacoes.estacao == a.estacao:
                            estacoes.distanciaAEstrela = a.distanciaAEstrela
            self.fronteira = sorted(self.fronteira, key=lambda a: a.distanciaAEstrela)

            pause = input("...")
            
            #Imprime a fronteira
            print("Lista de Fronteiras: ")
            for a in self.fronteira:
                print('{} - {}'.format(a.estacao.nome, a.distanciaAEstrela))
                
            if self.fronteira != None:
                proximaEstacao = self.fronteira[0].estacao
                self.fronteira.pop(0)
                pause = input("...")
                AEstrela.buscar(self, proximaEstacao)
                
from Mapa import Mapa

mapa = Mapa(14)
mapa.criarMapa()
aestrela = AEstrela(mapa.E14)
aestrela.buscar(mapa.E6)
print("Cidades Visitadas: ")
for cidades in aestrela.cidadesVisitadas:
    print(cidades.nome)
