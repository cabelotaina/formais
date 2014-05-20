def obter_duplas_com_sentencas_de_tamanho_n_mais_um(transicoes, duplas):
    novas_duplas = []

    for estado, sentenca in duplas:

        # obtem lista dos simbolos para os quais existe alguma transicao definida
        # partindo do 'estado' atual com qualquer um desses simbolos para algum estado do automato
        transicoes_selecionadas = [ (e,s,p) for ((e,s),p) in transicoes.iteritems() if e == estado ]

        for e, s, p in transicoes_selecionadas:
            novas_duplas.append((p, sentenca + s))

    return novas_duplas



def enumerarSentencas(M, n):

    # obtem todas as sentencas que podem ser geradas em um passo a partir do estado inicial
    # juntamente como o estado de destino ao se derivar do estado inicial com o simbolo em questao
    duplas = [ (p,s) for ((e,s),p) in M.transicoes.iteritems() if e == M.estado_inicial ]

    # repetir 'n' vezes
    for i in range(1, n):
        duplas = obter_duplas_com_sentencas_de_tamanho_n_mais_um(M.transicoes, duplas)

    # filtra as sentencas das duplas cujo estado for estado final
    sentencas = [ sentenca for estado, sentenca in duplas if estado in M.estados_finais and len(sentenca) == n ]

    sentencas.sort()
    
    return sentencas
