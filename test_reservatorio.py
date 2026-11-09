"""Verifica cores, mensagens e restauração do terminal na simulação."""

import io
import unittest
from contextlib import redirect_stdout
from colorama import Fore, Style
from Guilherme_Gomes_Justi_Ag11_DSI_Recup import definir_cor, exibir_situacao, main


class TestReservatorio(unittest.TestCase):
    def test_cinco_niveis_com_mensagem_cor_e_reset(self):
        esperados = [
            (1, Fore.RED, "Muito baixo (crítico)"),
            (2, Fore.YELLOW, "Baixo"),
            (3, Fore.GREEN, "Médio"),
            (4, Fore.CYAN, "Alto"),
            (5, Fore.BLUE, "Muito alto (alerta)"),
        ]
        for nivel, cor, mensagem in esperados:
            with self.subTest(nivel=nivel):
                self.assertEqual(definir_cor(nivel), cor)
                saida = io.StringIO()
                with redirect_stdout(saida):
                    exibir_situacao(nivel)
                self.assertEqual(saida.getvalue(), f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}\n")

    def test_niveis_invalidos(self):
        for nivel in [0, 6, -1]:
            with self.subTest(nivel=nivel):
                with self.assertRaises(ValueError):
                    definir_cor(nivel)

    def test_simulacao_exibe_os_cinco_niveis(self):
        saida = io.StringIO()
        with redirect_stdout(saida):
            main()
        for nivel in range(1, 6):
            self.assertIn(f"Nível {nivel}:", saida.getvalue())


if __name__ == "__main__":
    unittest.main()

