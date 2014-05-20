# -*- coding: utf-8 -*-

from Automato import Automato
from renomeador import renomear_estados

def juntarEstados(lista):
    lista = list(set(lista))
    lista.sort()
    lista = ''.join(lista)
    lista = lista.replace(',', '')
    return lista

def determinizar(AFN):
    '''
        Definicoes:
            um estado simples corresponde é a um estado original do AFN
            um estado composto corresponde é a composicao dos estados resultantes de uma transicao, se houver mais de um
    '''
    # se automato já é deterministico, não faz nada
    if AFN.deterministico:
        return AFN

    AFD = Automato()

    AFD.deterministico = True
    AFD.alfabeto = AFN.alfabeto
    AFD.estado_inicial = AFN.estado_inicial

    AFD.estados = [AFN.estado_inicial]

    for e in AFD.estados:
        for s in AFD.alfabeto:

            # tr vai armazenar os estados resultantes de todas as transições do símbolo 's' com os estados que compõem 'e'
            tr = []
            # se o estado 'e' for composto, repete para cada estado simples, 'ee', que o compoe
            for ee in e:
                if (ee,s) in AFN.transicoes:
                    # adiciona todos os estados resultantes de derivacoes de 'e' a 'tr'
                    tr.extend(AFN.transicao(ee,s))

            # cria um estado 'p', que eh a composicao das transicoes (e,s)
            p = juntarEstados(tr)

            if not p: continue

            AFD.adicionarTransicao(e, s, p)

    # adiciona aos estados finais se um estado eh composto de algum estado final do AFN
    AFD.estados_finais = [ e for e in AFD.estados if [ p for p in AFN.estados_finais if p in list(e) ] ]

    return renomear_estados(AFD)