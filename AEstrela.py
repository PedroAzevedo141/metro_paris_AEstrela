from VetorOrdenadoAdjacente import VetorOrdenadoAdjacente

class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.fronteira = None
        self.achou = False

    def buscar(self, atual):
        print('-----------------------------------')
        print('\nAtual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            print('Fronteira: {}'.format(self.fronteira.mostrar()))
            for a in atual.adjacentes:
                if a.estacao.visitado == False:
                    a.estacao.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            print(self.fronteira)
            if self.fronteira.getPrimeiro() != None:
                AEstrela.buscar(self, self.fronteira.getPrimeiro())
                
from Mapa import Mapa

mapa = Mapa(14)
mapa.criarMapa()
aestrela = AEstrela(mapa.E14)
aestrela.buscar(mapa.E1)
