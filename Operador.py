from Automato import Automato
from determinizador import Determinizador
from Minimizador import Minimizador
from renomeador import renomear_estados
import completador

class Operador:

    def obterComplemento(self, automato):
        # completa automato, preenchendo transicoes faltantes com transicoes para o estado de erro ('-')
        M = completador.completar(automato)

        # todos os estados nao-finais passam a ser finais
        M.estados_finais = [e for e in M.estados if e not in M.estados_finais ]

        M = completador.remover_estado_erro(automato)

        return M


    def obterUniao(self, A, B):
        M = AutomatoImpl()
        M.estado_inicial = 'S'
        M.alfabeto = list(set(A.alfabeto[:] + B.alfabeto[:]))

        novo_nome_estados_B = [ 'B' + e for e in B.estados ]
        novo_nome_estados_finais_B = [ 'B' + e for e in B.estados_finais ]
        novo_nome_transicoes_B = { (('B'+e),s):('B' + p) for ((e,s),p) in B.transicoes.iteritems() }
        novo_nome_estado_inicial_B = 'B' + B.estado_inicial
        
        M.estados = A.estados[:] + novo_nome_estados_B
        M.estados_finais = A.estados_finais[:] + novo_nome_estados_finais_B

        transicoes_A = { (e,s):p for ((e,s),p) in A.transicoes.iteritems() if e != A.estado_inicial }
        transicoes_B = { (e,s):p for ((e,s),p) in novo_nome_transicoes_B if e != novo_nome_estado_inicial_B }
        M.transicoes = dict(transicoes_A.items() + transicoes_B.items())

        for s in M.alfabeto:
            proximos = []
            if (A.estado_inicial, s) in A.transicoes:
                proximos.extend(A.transicoes[(A.estado_inicial, s)])
            if (novo_nome_estado_inicial_B, s) in novo_nome_transicoes_B:
                proximos.extend(novo_nome_transicoes_B[(novo_nome_estado_inicial_B, s)])
            if len(proximos) > 1:
                M.deterministico = False
            M.transicoes[(M.estado_inicial, s)] = ','.join(proximos)

        M_min = MinimizadorImpl().minimizar(M)
        return renomear_estados(M_min)
        

    def obterInterseccao(self, A, B):
        not_A = self.obterComplemento(A)
        not_B = self.obterComplemento(B)
        
        uniao_complementos = self.obterUniao(not_A, not_B)
        interseccao = self.obterComplemento(uniao_complementos)        

        return interseccao
