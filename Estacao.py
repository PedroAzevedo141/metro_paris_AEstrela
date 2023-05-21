class Estacao:
    def __init__(self, nome, distanciaObjetivo):
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo
        self.nome = nome    
        self.adjacentes = []
        self.pai = None
        
    def addEstacaoAdjacente(self, estacao):
        self.adjacentes.append(estacao)