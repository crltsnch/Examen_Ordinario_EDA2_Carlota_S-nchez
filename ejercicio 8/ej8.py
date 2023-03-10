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
for node in g.nodes():
    for i in range(4):
        other_node = random.choice(list(g.nodes()))   #elegimos al azor otro nodo (planeta)
        while other_node == node:     #si es el mismo, volvemos a elegir
            other_node = random.choice(list(g.nodes()))
        weight = random.randint(1, 10)   #elegimos un peso al azar
        g.add_edge(node, other_node, weight=weight)   #agregamos la arista entre el nodo actual y el nodo elegido

t = nx.minimum_spanning_tree(g)   #obtenemos el arbol de expansion minima

#distancias
distance1 = nx.shortest_path_length(t, source = 'Tatooine', target='Dagobah', weight='weight')   #obtenemos la distancia entre Tatooine y Dagobah
distance2 = nx.shortest_path_length(t, source = 'Alderaan', target='Endor', weight='weight')
distance3 = nx.shortest_path_length(t, source = 'Hoth', target='Tatooine', weight='weight')

print(distance1)
print(distance2)
print(distance3)

#determinamos todos los planetas a los que se puede llegar desde Tatooine
neighbors =list(t.neighbors('Tatooine'))   #obtenemos los vecinos de Tatooine
print('Los planetas a los que se puede llegar desde Tatooine son: ', neighbors)
