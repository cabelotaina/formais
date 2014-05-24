# -*- coding: utf-8 -*-

import string

def nomes_novos_estados(quantidade):
    assert quantidade <= 676, 'Quantidade máxima excedida (estados possíveis: [A-ZZ])'

    letras = list(string.ascii_uppercase)
    del letras[18]
    letras.insert(0, 'S')
    lista = []
    for i in range(0, quantidade):
        indice_prefixo =  i // len(letras)
        indice_letra = i - (indice_prefixo * len(letras))
        prefixo = ''
        if indice_prefixo > 0:
            prefixo = letras[indice_prefixo]

        letra = letras[indice_letra ]
        lista.append( prefixo + letra)
    return lista


def renomear_automato(automato):
    novos_nomes = nomes_novos_estados(len(automato.estados))
    antigos_nomes = [ automato.estado_inicial ] + list(automato.estados.difference({automato.estado_inicial}))
    renomear = { antigo:novo for antigo,novo in zip(antigos_nomes, novos_nomes) }
    automato.atributos['mapa_renomear'] = renomear

    novo_estado_inicial = renomear[automato.estado_inicial]
    novos_estados = { renomear[estado] for estado in automato.estados }
    novos_estados_finais = { renomear[estado_final] for estado_final in automato.estados_finais }
    novas_transicoes = {}
    for (estado, simbolo), proximos_estados in automato.transicoes.iteritems():
        novas_transicoes[(renomear[estado], simbolo)] = set()
        for proximo_estado in proximos_estados:
            novas_transicoes[(renomear[estado], simbolo)].add(renomear[proximo_estado])

    automato.estados = novos_estados
    automato.estado_inicial = novo_estado_inicial
    automato.estados_finais = novos_estados_finais
    automato.transicoes = novas_transicoes