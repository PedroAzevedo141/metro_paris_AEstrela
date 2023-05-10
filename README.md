# Desafio do mapa “reduzido” do metrô de Paris

## Quick Start

```bash
python .\AEstrela.py
```

## Informações

- Ao rodar esse codigo, ele automaticamente ira gerar o melhor caminha entre A1 ate A14, para mudar, entre no arquivo AEstrela.py e mude a variavel <aestrela = AEstrela(mapa.E14)> para o que desejar. Exemplo: <aestrela = AEstrela(mapa.A1)>
- O mesmo para <aestrela.buscar(mapa.E1)> para o que desejar. Exemplo: <aestrela.buscar(mapa.A2)>
- O motivo da solução desse desafio, junto com o do puzzle dos 8 números, foi desenvolver um algoritmo de busca A* sem a utilização da lista aberta e fechada, apenas com a utilização de uma lista de prioridade. E levando a um dos motivos da nescessidade da utilização dessas listas, que é a de não passar por um mesmo nó duas vezes, o que pode gerar um loop infinito ou a estagnação do algoritmo.

