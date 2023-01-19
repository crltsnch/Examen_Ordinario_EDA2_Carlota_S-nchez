import networkx as nx

grafo = nx.Graph()   #grafo vacío
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Cantonica', 'DQar', 'Dantooine', 'Atollon', 'Jedha', 'Corellia', 'Coruscant']
grafo.add_nodes_from(planetas)

#agregamos las aristas con el metodo add_edge()
grafo.add_edge('Alderaan', 'Endor')



