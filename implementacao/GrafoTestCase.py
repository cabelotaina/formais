# -*- coding: utf-8 -*-

import unittest
from Grafo import Grafo
from AutomatoFinito import AutomatoFinito

class GrafoTestCase(unittest.TestCase):

    def test_criacao_grafo_a_partir_de_automato_finito(self):
        automato = AutomatoFinito(gramatica='S -> aS | bB | cC | a | b | c'
                                          '\nB -> bB | cC | b | c'
                                          '\nC -> cC | c')
        grafo = Grafo(automato)
        inicial = automato.estado_inicial
        finais = automato.estados_finais
        self.assertEqual(grafo.existe_caminho_entre_vertices(inicial, finais), False)


if __name__ == '__main__':
    unittest.main()
