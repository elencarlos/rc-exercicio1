import networkx as nx
import collections
import numpy as np
import matplotlib.pyplot as plt
from grafo import Grafo

if __name__ == "__main__":
    g = {
        "a": ["c", "d", "f"],
        "b": ["c"],
        "c": ["a", "b", "d"],
        "d": ["a", "c", "e", "f"],
        "e": ["d", "f", "g", "h"],
        "f": ["a", "d", "e"],
        "g": ["e", "h"],
        "h": ["e", "g"]
    }

    grafo = Grafo(g)

    G = nx.Graph(grafo.arestas())

    """
    a) Defina a distribuicao empirica do grau do grafo. Faca um grafico da distribuicao
    empirica do grau do grafo (usando CCDF, P[G > k]). Determine o grau medio.
    """
    # distribuicao empirica do grau
    deg, cnt, dis, ccdf = grafo.distribuicao()

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')
    plt.title("Distribuicao")
    plt.ylabel("grau k")
    plt.xlabel("Grau")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.show()

    print(".:Distribuicao")
    for i in range(len(grafo.vertices())):
        print("Grau %s => %.02f" % (i, dis[i]))


    plt.stem(range(len(grafo.vertices())),dis, "g")
    plt.title("Distribuicao do grau")
    plt.ylabel("grau k")
    plt.xlabel("Grau")
    plt.show()

    plt.plot(range(len(grafo.vertices())), ccdf, "bo")
    plt.grid(True)
    plt.title("CCDF")
    plt.ylabel("grau > k")
    plt.xlabel("Grau")
    plt.show()

    """"
    b) distacia        
    """

    print(grafo.distancia_matriz())

    

    # grafo
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='pink', alpha=0.9,
            labels={node: str(node).upper() for node in G.nodes()})
    plt.show()
