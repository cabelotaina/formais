# -*- coding: utf-8 -*-

import unittest
from AutomatoFinito import AutomatoFinito
from constantes import *


class EstruturaAutomatoFinitoTestCase(unittest.TestCase):

    def setUp(self):
        self.AutomatoFinitoVazio = AutomatoFinito()

    def test_automato_finito_tem_um_conjunto_de_estados(self):
        self.assertTrue(hasattr(self.AutomatoFinitoVazio, 'estados'), "Autômato não tem atributo 'estados'")
        self.assertEquals(self.AutomatoFinitoVazio.estados, set(), "Estados do autômato não são um conjunto")

    def test_automato_finito_tem_um_conjunto_de_simbolos(self):
        self.assertTrue(hasattr(self.AutomatoFinitoVazio, 'alfabeto'), "Autômato não tem atributo 'alfabeto'")
        self.assertEquals(self.AutomatoFinitoVazio.alfabeto, set(), "Alfabeto do autômato não é um conjunto")

    def test_automato_finito_tem_um_dicionario_de_transicoes(self):
        self.assertTrue(hasattr(self.AutomatoFinitoVazio, 'transicoes'), "Autômato não tem atributo 'transicoes'")
        self.assertEquals(self.AutomatoFinitoVazio.transicoes, dict(), "Transições do autômato não são um dicionário (mapa de hash)")

    def test_automato_finito_tem_um_estado_inicial(self):
        self.assertTrue(hasattr(self.AutomatoFinitoVazio, 'estado_inicial'), "Autômato não tem atributo 'estado_inicial'")
        self.assertEquals(self.AutomatoFinitoVazio.estado_inicial, None, "Estado inicial do autômato deve ser um elemento único")

    def test_automato_finito_tem_um_conjunto_de_estados_finais(self):
        self.assertTrue(hasattr(self.AutomatoFinitoVazio, 'estados_finais'), "Autômato não tem atributo 'estados_finais'")
        self.assertEquals(self.AutomatoFinitoVazio.estados_finais, set(), "Estados finais do autômato não são um conjunto")

class AlgoritmosAutomatoFinitoTestCase(unittest.TestCase):

    def test_gerar_automato_a_partir_de_gramatica(self):
        automato_em_teste = AutomatoFinito(gramatica='S -> aS | a | bA \nA -> aA | a | bS')

        transicoes = {}
        transicoes[('S', 'a')] = { 'S', estado_final_algoritmo_gramatica }
        transicoes[('S', 'b')] = { 'A' }
        transicoes[('A', 'a')] = { 'A', estado_final_algoritmo_gramatica }
        transicoes[('A', 'b')] = { 'S' }
        transicoes[(estado_final_algoritmo_gramatica), 'a'] = set()
        transicoes[(estado_final_algoritmo_gramatica), 'b'] = set()

        self.assertEquals(automato_em_teste.estados, {'S', 'A', estado_final_algoritmo_gramatica})
        self.assertEquals(automato_em_teste.alfabeto, {'a', 'b'})
        self.assertEquals(automato_em_teste.transicoes, transicoes)
        self.assertEquals(automato_em_teste.estado_inicial, 'S')
        self.assertEquals(automato_em_teste.estados_finais, {estado_final_algoritmo_gramatica})


    def test_obter_automato_reverso(self):
        automato_original = AutomatoFinito(gramatica='S -> aS | bB | cC | a | b | c'
                                                   '\nB -> bB | cC | b | c'
                                                   '\nC -> cC | c')

        automato_reverso = automato_original.obter_reverso()

        transicoes = {}
        for estado in automato_reverso.estados:
            for simbolo in automato_reverso.alfabeto:
                transicoes[(estado, simbolo)] = set()

        transicoes[('S', 'a')] = { 'S' }
        transicoes[('B', 'b')] = { 'S', 'B'}
        transicoes[('C', 'c')] = { 'S', 'B', 'C'}
        transicoes[(estado_final_algoritmo_gramatica, 'a')] = { 'S' }
        transicoes[(estado_final_algoritmo_gramatica, 'b')] = { 'S', 'B' }
        transicoes[(estado_final_algoritmo_gramatica, 'c')] = { 'S', 'B', 'C' }

        self.assertEquals(automato_reverso.estados, {'S', 'B', 'C', estado_final_algoritmo_gramatica})
        self.assertEquals(automato_reverso.alfabeto, {'a', 'b', 'c'})
        self.assertEquals(automato_reverso.transicoes, transicoes)
        self.assertEquals(automato_reverso.estado_inicial, estado_final_algoritmo_gramatica)
        self.assertEquals(automato_reverso.estados_finais, { 'S' })


if __name__ == '__main__':
    unittest.main()
