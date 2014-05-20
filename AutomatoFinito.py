# -*- coding: utf-8 -*-

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
        novo_estado_final = 'Novo Estado Final'
        self.estados.add(novo_estado_final)
        self.estados_finais.add(novo_estado_final)

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
            # remover espaços
            estado, producoes = linha.split('->')
            for producao in producoes.split('|'):
                if len(producao) == 1:
                    self.transicoes[(estado, producao)].add(novo_estado_final)
                elif len(producao) == 2:
                    terminal = producao[0]
                    nao_terminal = producao[1]
                    self.transicoes[(estado,terminal)].add(nao_terminal)

                elif estado == self.estado_inicial and producao == 'epsilon':
                    self.estados_finais.add(estado)

    def definido_a_partir_de_expressao_regular(self, str):
        raise NotImplementedError

    def determinizar(self):
        raise NotImplementedError

    def minimo(self):
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
        raise NotImplementedError

    def enumerar_sentencas(self, tamanho):
        raise NotImplementedError

    def determinar_finitude(self):
        # veerificar se é melhor fazer assim ou crar três métodos vazia/finita/infinita
        raise NotImplementedError

A = AutomatoFinito(gramatica='S->aS|a|bA\nA->aA|a|bS')
B = AutomatoFinito(expressao_regular='(ab)*b?(aaa)+')
C = AutomatoFinito()
print A.eh_igual(B)
print A.obter_complemento()

