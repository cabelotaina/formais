from determinizador import Determinizador

class Minimizador:
    def minimizar( self, M ):

        if not M.deterministico:
            D = DeterminizadorImpl()
            M = D.determinizar(M)

        #======== Remover estados inalcancaveis ==========================================================================================#

        # obtem lista de todos os estados que aparecem do lado direito de nenhuma transicao
        alcancaveis = [ e for e in M.estados if e in M.transicoes.values( ) or e == M.estado_inicial ]

        # remove todas as transicoes que partem o chegam em estados inalcancaveis
        M.transicoes = { (e, s): p for ((e, s), p) in M.transicoes.iteritems( ) if p in alcancaveis and e in alcancaveis }

        # remove todos os estados que sao inalcancaveis    
        M.estados = alcancaveis


        #======== Remover estados mortos =================================================================================================#

        # estados finais sao vivos por definicao
        vivos = M.estados_finais[ : ]
        for v in vivos:
            # adiciona a 'vivos' os estados para os quais existe alguma derivacao para um estado vivo
            vivos.extend( [ p for ((e, s), p) in M.transicoes.iteritems( ) if e == v and p not in vivos ] )

        # remove todas as transicoes que nao partem ou chegam em estados vivos
        M.transicoes = { (e, s): p for ((e, s), p) in M.transicoes.iteritems( ) if e in vivos or p in vivos }

        M.estados = vivos

        #======== Remover simbolos nao usados em nenhuma transicao =======================================================================#

        # obtem lista de todos os simbolos que aparecem em alguma transicao
        simbolos = [ s for (e, s) in M.transicoes.keys( ) ]

        # remove simbolos diplicados
        simbolos = list( set( simbolos ) )
        simbolos.sort( )

        M.alfabeto = simbolos

        #======== Remover estados equivalentes ===========================================================================================#

        T = M.transicoes
        T[ ('G', 'a') ] = 'G'

        classes = [ ]
        classes.append( [ e for e in M.estados if e not in M.estados_finais ] )
        classes.append( M.estados_finais[ : ] )

        novas = [ ]

        while novas != classes:
            novas = [ ]

            Q = { }
            for classe in classes:
                for e in classe:
                    Q[ e ] = classe

            for classe in classes:
                if len(classe) == 1:
                    novas.append(classe)
                elif len(classe) > 0:
                    c = classe[ 0 ]
                    equivalentes = [ e for e in classe if all( [ (c, s) in T.keys() and (e, s) in T.keys() and Q[T[c,s]] == Q[T[e,s]] for s in M.alfabeto ] ) ]
                    nao_equivalentes = [ e for e in classe if e not in equivalentes ]

                    if equivalentes:
                        novas.append( equivalentes )
                    if nao_equivalentes:
                        classes.append( nao_equivalentes )

            classes = novas

        renomear = {}
        for classe in classes:
            for c in classe:
                renomear[c] = classe[0]

        M.estados = list(set(renomear.values()))
        M.estados_finais = [ e for e in M.estados_finais if e in M.estados ]
        M.estado_inicial = renomear[M.estado_inicial]

        transicoes = { (e,s):renomear[p] for ((e,s),p) in M.transicoes.iteritems() if e in M.estados  }
        M.transicoes = { (e,s):transicoes[(e,s)] for (e,s) in set(transicoes.keys()) }
        
        return M
