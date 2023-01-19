import networkx as nx
import random

g = nx.Graph()   #grafo vacío
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Cantonica', 'DQar', 'Dantooine', 'Atollon', 'Jedha', 'Corellia', 'Coruscant']

g.add_node('Alderaan')
g.add_node('Endor')
g.add_node('Dagobah')
g.add_node('Hoth')
g.add_node('Tatooine')
g.add_node('Kamino')
g.add_node('Naboo')
g.add_node('Mustafar')
g.add_node('Scarif')
g.add_node('Bespin')
g.add_node('Cantonica')
g.add_node('DQar')
g.add_node('Dantooine')
g.add_node('Atollon')
g.add_node('Jedha')
g.add_node('Corellia')
g.add_node('Coruscant')

#generamso al menos 4 aristas
for i in range(4):
    other_node = random.coice(list(g.nodes()))   #elegimos al azor otro nodo (planeta)
    while other_node == node:
        other_node = random.choice(list(g.nodes()))