import networkx as nx
import random

grafo = nx.Graph()   #grafo vacío
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Cantonica', 'DQar', 'Dantooine', 'Atollon', 'Jedha', 'Corellia', 'Coruscant']
grafo.add_nodes_from(planetas)

#agregamos 4 aristar por cada planeta
def agregar_aristas(grafo, planetas):
    for planeta in planetas:
        for i in range(4):
            planeta_aleatorio = random.choice([p for p in planetas if p != planeta])
            grafo.add_edge(planeta, planeta_aleatorio)
    return grafo

#algoritmo de Kruskal
