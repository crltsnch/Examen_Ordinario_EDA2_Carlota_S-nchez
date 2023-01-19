import networkx as nx

grafo = nx.Graph()   #grafo vacío
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Cantonica', 'DQar', 'Dantooine', 'Atollon', 'Jedha', 'Corellia', 'Coruscant']
grafo.add_nodes_from(planetas)


