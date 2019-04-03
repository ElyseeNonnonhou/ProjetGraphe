# -*- coding: utf-8 -*-
import networkx as nx 
from matplotlib import pyplot as plt
import csv 

#Creation d'un Graphe vide
G = nx.Graph() 

#On cree les arrêtes du Graphe en récupérant les sommets dans le fichier distance.csv
with open('C:\Users\dorin\Desktop\py\distance.csv') as csvfile: 
        csv_reader = csv.reader(csvfile,delimiter=',')
        for rows in csv_reader: 
            node_prev = G.add_node(rows[0],pos=(float(rows[2]),float(rows[3])))
            node_next = G.add_node(rows[1]) 
            G.add_edge(rows[0],rows[1])
        d = nx.coloring.greedy_color(G, strategy=nx.coloring.strategy_largest_first)
        print d
        pos=nx.get_node_attributes(G,'pos')
            
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_nodes(G,pos)
        nx.draw_networkx_nodes(G,pos)
        #nx.draw_networkx_labels(G,pos)
        nx.draw_networkx_edges(G,pos)
        #nx.draw(G)
        plt.show()

      