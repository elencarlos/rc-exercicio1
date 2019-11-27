import collections

import numpy as np

""" Classe Python simples que demostra um grafo
"""


class Grafo(object):
    def __init__(self, grafo_dic=None):
        if grafo_dic == None:
            grafo_dic = {}
        self.__grafo = grafo_dic

    def vertices(self):
        return self.__grafo.keys()

    def arestas(self):
        return self.__gera_arestas()

    def add_vertice(self, vertice):
        if vertice not in self.__grafo:
            self.__grafo[vertice] = []

    def add_aresta(self, aresta):
        aresta = set(aresta)
        (v1, v2) = tuple(aresta)
        if v1 in self.__grafo:
            self.__grafo[v1].append(v2)
        else:
            self.__grafo[v1] = [v2]

    def __gera_arestas(self):
        arestas = []
        for vertice in self.__grafo:
            for vizinho in self.__grafo[vertice]:
                if {vizinho, vertice} not in arestas:
                    arestas.append({vertice, vizinho})
        return arestas

    def adj(self, vertice):
        return self.__grafo[vertice]

    def v_grau(self, vertice):
        """ Quantidade de conexoes do vertice, conta dobrado
        """
        adj_vertices = self.__grafo[vertice]
        degree = len(adj_vertices) + adj_vertices.count(vertice)
        return degree

    def v_grau_all(self):
        for vertice in self.__grafo:
            grau = self.v_grau(vertice)
            print("vertice %s : %.03f" % (vertice, grau))

    def grau_medio(self):
        m = 0
        grau = 0
        for vertice in self.__grafo:
            grau += self.v_grau(vertice)
            m += 1
        grau_medio = grau / m
        return grau_medio

    def distribuicao(self):
        """
        numero de arestas com grau k/numero total de vertices
        """
        degrees = [self.v_grau(n) for n in self.vertices()]
        degree_sequence = sorted([d for d in degrees], reverse=True)
        degreeCount = collections.Counter(degree_sequence)
        deg, cnt = zip(*degreeCount.items())

        dis = np.zeros(len(self.vertices()))
        for v in self.vertices():
            dis[self.v_grau(v)] += 1
        dis /= len(self.vertices())

        ccdf = [sum(dis[i + 1:]) for i in range(len(self.vertices()))]

        return deg, cnt, dis, ccdf

    def caminho(self, start_vertex, end_vertex, path=[]):
      graph = self.__grafo
      path = path + [start_vertex]
      if start_vertex == end_vertex:
          return [path]
      if start_vertex not in graph:
          return []
      paths = []
      for vertex in graph[start_vertex]:
          if vertex not in path:
              extended_paths = self.caminho(vertex, 
                                                    end_vertex, 
                                                    path)
              for p in extended_paths: 
                  paths.append(p)
      return paths

    def distancia_matriz(self):
      grafo = self
      distancias = {}
      for start in grafo.vertices():
        distancias[start] = {}
        for end in grafo.vertices():
            if isinstance(grafo.caminho(start,end), list):
              for d in grafo.caminho(start,end):
                if(distancias[start][end] >= (len(d)-1) )
                  distancias[start][end] = len(d)-1
            else:    
            distancias[start][end] = len(grafo.caminho(start,end))-1
      
      return distancias
      

    def distancia_media(self):
        pass

    def clusterizacao(self):
        pass

    def clusterizacao_all(self):
        pass

    def clusterizacao_media(self):
        pass

    def __str__(self):
        res = "vertices: "
        for k in self.__grafo:
            res += str(k) + " "
        res += "\narestas: "
        for aresta in self.__gera_arestas():
            res += str(aresta) + " "
        return res
