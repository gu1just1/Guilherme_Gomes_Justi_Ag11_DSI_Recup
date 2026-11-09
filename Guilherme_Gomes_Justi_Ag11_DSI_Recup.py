"""Agenda 11 - Recuperação de Desenvolvimento de Sistemas I.

Simulação dos cinco níveis de água de um reservatório no terminal.
Autor: Guilherme Gomes Justi.
"""

from colorama import Fore, Style, init


# A posição de cada mensagem corresponde ao nível menos um.
mensagens = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]


def definir_cor(nivel):
    """Retorna a cor do nível informado, que deve estar entre 1 e 5."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        raise ValueError("O nível deve estar entre 1 e 5.")


def exibir_situacao(nivel):
    """Mostra a situação com sua cor e restaura o estilo do terminal."""
    cor = definir_cor(nivel)
    mensagem = mensagens[nivel - 1]
    print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")


def main():
    """Percorre os níveis definidos no código, sem solicitar entrada."""
    niveis_simulados = [1, 2, 3, 4, 5]
    print("CONTROLE DE NÍVEIS DE ÁGUA")
    print("Simulação do reservatório\n")
    for nivel in niveis_simulados:
        exibir_situacao(nivel)
    print("\nSimulação encerrada. Estilo padrão restaurado.")


if __name__ == "__main__":
    # Inicializa o suporte a cores, inclusive nos terminais do Windows.
    init()
    main()

