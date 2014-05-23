# -*- coding: utf-8 -*-

from constantes import *
from Grafo import Grafo

class AutomatoFinito:
    def __init__(self, gramatica=None, expressao_regular=None):
        self.estados= set()
        self.alfabeto = set()
        self.estado_inicial = None
        self.estados_finais = set()
        self.transicoes = {}

        if gramatica: self.definido_a_partir_de_gramatica(gramatica)
        elif expressao_regular: self.definido_a_partir_de_expressao_regular(expressao_regular)

    def definido_a_partir_de_gramatica(self, str):
        self.estados.add(estado_final_algoritmo_gramatica)
        self.estados_finais.add(estado_final_algoritmo_gramatica)

        # popula estados, alfabeto e estado inicial
        for s in str:
            if s.islower():
                self.alfabeto.add(s)
            if s.isupper():
                self.estados.add(s)
                if not self.estado_inicial:
                    self.estado_inicial = s

        # inicializa as transições com o conjunto de estados de destino vazio
        for estado in self.estados:
            for simbolo in self.alfabeto:
                self.transicoes[(estado, simbolo)] = set()

        linhas = str.split('\n')
        for linha in linhas:
            linha = ''.join(linha.split())
            estado, producoes = linha.split(simbolo_implicacao_gramatica)
            for producao in producoes.split(simbolo_ou_gramatica):
                if len(producao) == 1:
                    self.transicoes[(estado, producao)].add(estado_final_algoritmo_gramatica)
                elif len(producao) == 2:
                    terminal = producao[0]
                    nao_terminal = producao[1]
                    self.transicoes[(estado,terminal)].add(nao_terminal)

                elif estado == self.estado_inicial and producao == epsilon:
                    self.estados_finais.add(estado)

    def definido_a_partir_de_expressao_regular(self, str):
        raise NotImplementedError

    def determinizar(self):
        raise NotImplementedError

    def minimo(self):
        # minimizar o autômato usand o reverso e determinístico (algoritmo de Brzozowski)
        raise NotImplementedError

    def eh_igual(self, outro_automato):
        raise NotImplementedError

    def obter_complemento(self):
        raise NotImplementedError

    def obter_interseccao(self, outro_automato):
        raise NotImplementedError

    def obter_diferenca(self, outro_automato):
        raise NotImplementedError

    def obter_reverso(self):
        novo_estado_inicial = ''.join(self.estados_finais)

        NovoAutomato = AutomatoFinito()
        NovoAutomato.estados = self.estados.union({novo_estado_inicial})
        NovoAutomato.alfabeto = self.alfabeto.union({})
        # inverte estado final com estados finais (novo estado final é um estado
        NovoAutomato.estado_inicial = novo_estado_inicial
        NovoAutomato.estados_finais = { self.estado_inicial }

        # inicializa as transições
        for estado in NovoAutomato.estados:
            for simbolo in NovoAutomato.alfabeto:
                NovoAutomato.transicoes[(estado, simbolo)] = set()

        # cria as transições reversas
        for ((estado, simbolo), proximos_estados) in self.transicoes.iteritems():
            for proximo_estado in proximos_estados:
                NovoAutomato.transicoes[(proximo_estado, simbolo)].add(estado)

        # adiciona epsilon-transições dos antigos estados finais para um novo estado final
        if len(self.estados_finais) > 1:
            NovoAutomato.transicoes.update( { (estado_final, epsilon):{novo_estado_inicial} for estado_final in self.estados_finais } )

        return NovoAutomato

    def enumerar_sentencas(self, tamanho=0):
        # obtem todas as sentencas que podem ser geradas em um passo a partir do estado inicial
        # juntamente como o estado de destino ao se derivar do estado inicial com o simbolo em questao

        duplas = { (self.estado_inicial, simbolo) for simbolo in self.alfabeto }
        # a cada iteração, obtém sentencas de tamanho i
        for i in range(1, tamanho):
            novas_duplas = set()
            for estado_atual, sentenca in duplas:
                for ((estado, simbolo), proximos_estados) in self.transicoes.iteritems():
                    for proximo_estado in proximos_estados:
                        if estado_atual == estado:
                            novas_duplas.add((proximo_estado, sentenca + simbolo))
            duplas = novas_duplas

        # filtra as sentencas das duplas cujo estado for estado final
        sentencas = { sentenca for estado_atual, sentenca in duplas if estado_atual in self.estados_finais }

        return sentencas

    def eh_vazio(self):
        grafo = Grafo(automato=self)
        return not grafo.existe_caminho_entre_vertices(self.estado_inicial, self.estados_finais)

    def eh_finito(self):
        grafo = Grafo(automato=self)
        return not grafo.tem_ciclos(vertice_inicial=self.estado_inicial)
