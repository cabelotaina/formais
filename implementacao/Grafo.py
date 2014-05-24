# -*- coding: utf-8 -*-

from Vertice import Vertice
from constantes import *

class Grafo:
    def __init__(self, automato):
        # vs é um mapa que relaciona o nome de um estado do automato com um vértice do grafo
        vs = {}

        self.vertices = set()
        self.atributos = { mapa_nomes_vertices : vs }

        for estado in automato.estados:
            vertice = Vertice(estado)
            vs[estado] = vertice
            self.vertices.add(vertice)

        for ((estado, simbolo), proximos) in automato.transicoes.iteritems():
            vertice = vs[estado]
            for proximo in proximos:
                sucessor = vs[proximo]
                vertice.adicionar_sucessor(sucessor)


    # busca um Vertice pelo nome
    def obter_vertice(self, nome):
        return self.atributos[mapa_nomes_vertices][nome]



    def existe_caminho_entre_vertices(self, nome_vertice_inicial, nomes_vertices_finais):
        lista_busca = [self.obter_vertice(nome_vertice_inicial)]

        vertices_finais_nao_visitados = { self.obter_vertice(nome) for nome in nomes_vertices_finais }
        assert len(vertices_finais_nao_visitados) > 0, 'não existe nenhum vértice final!'

        for vertice in self.vertices:
            vertice.set(status, NAO_VISITADO)

        vertice_inicial = self.obter_vertice(nome_vertice_inicial)
        vertice_inicial.set(status, JA_VISITADO)
        
        while len(lista_busca) > 0:
            vertice = lista_busca.pop(0)
            for sucessor in vertice.sucessores():
                if sucessor.get(status) == NAO_VISITADO:
                    lista_busca.append(sucessor)
                    vertices_finais_nao_visitados.discard(vertice)
                    sucessor.set(status, JA_VISITADO)

        return len(vertices_finais_nao_visitados) == 0



    def tem_ciclos(self, vertice_inicial):
        for vertice in self.vertices:
            vertice.set(status, NAO_VISITADO)

        inicial = self.obter_vertice(vertice_inicial)
        inicial.set(status, JA_VISITADO)
        lista_busca = [ inicial ]

        while len(lista_busca) > 0:
            vertice = lista_busca.pop(0)
            for sucessor in vertice.sucessores():
                if sucessor.get(status) == NAO_VISITADO:
                    sucessor.set(status, JA_VISITADO)
                    lista_busca.append(sucessor)

                elif vertice.get(status) == JA_VISITADO:
                    return True

        return False
