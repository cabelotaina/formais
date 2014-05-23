# -*- coding: utf-8 -*-

class Vertice:
    def __init__(self, nome, sucessores=set()):
        self.nome = nome
        self.atributos = {}
        self._sucessores = sucessores

    # retorna uma representação textual do vértice
    def __str__(self):
        atributos = ', '.join([ k +'='+ v for k,v in self.atributos.iteritems()])
        return '{0} : {}'.format(self.nome, atributos)

    # define a função hash, para permitir usar um Vertice como chave num mapa de hash
    def __hash__(self):
        return hash(self.nome)

    # função de comparação de Vertices, para permitir testes do tipo (Vertice_a == Vertice_b)
    def __cmp__(self, other):
        return cmp(self.nome, other.nome)

    # permite associar um objeto (hasheable) no Vertice
    def set(self, chave, valor):
        setattr(self.atributos, chave, valor)

    # busca um objeto associado ao Vertice
    def get(self, chave):
        return getattr(self.atributos, chave, None)

    # adiciona um Vertice à lista de sucessores
    def adicionar_sucessor(self, vertice):
        assert isinstance(vertice, Vertice), 'não é permitido adicionar um objeto que não seja do tipo Vertice'
        self._sucessores.add(vertice)

    # retorna a lista de Vertices sucessores
    def sucessores(self):
        return self._sucessores
