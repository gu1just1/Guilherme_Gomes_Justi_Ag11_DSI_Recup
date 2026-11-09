# Controle de Níveis de Água

**Autor:** Guilherme Gomes Justi  
**Curso:** Desenvolvimento de Sistemas - EaDTEC / Centro Paula Souza  
**Atividade:** Agenda 11 - Desenvolvimento de Sistemas I - Recuperação

## Objetivo

Simular no terminal o monitoramento de um reservatório e exibir uma mensagem colorida para cada um dos cinco níveis de água. Os valores são definidos no código, sem entrada do usuário.

| Nível | Situação | Cor do Colorama |
| --- | --- | --- |
| 1 | Muito baixo (crítico) | `Fore.RED` - vermelho |
| 2 | Baixo | `Fore.YELLOW` - amarelo |
| 3 | Médio | `Fore.GREEN` - verde |
| 4 | Alto | `Fore.CYAN` - ciano |
| 5 | Muito alto (alerta) | `Fore.BLUE` - azul |

## Como executar

É necessário ter Python 3 instalado. Abra um terminal na pasta do projeto e execute:

```bash
python -m pip install -r requirements.txt
python Guilherme_Gomes_Justi_Ag11_DSI_Recup.py
```

Em instalações do Windows que usam o comando `py`, substitua `python` por `py`. Execute em um terminal com suporte a cores. Ao redirecionar a saída para um arquivo, o Colorama pode remover os códigos de cor.

## Organização e desenvolvimento

1. Importe `Fore`, `Style` e `init` da biblioteca Colorama.
2. Armazene as cinco situações na lista `mensagens`, da menor para a maior altura da água.
3. A função `definir_cor(nivel)` seleciona a cor usando `if`, `elif` e `else`. Níveis fora de 1 a 5 geram `ValueError`.
4. A função `exibir_situacao(nivel)` obtém a mensagem pela posição `nivel - 1`, acrescenta a cor e imprime o alerta.
5. Cada mensagem termina com `Style.RESET_ALL`, restaurando a aparência padrão do terminal.
6. A função `main()` percorre a lista `niveis_simulados` com os valores `[1, 2, 3, 4, 5]`. O bloco final inicializa o Colorama com `init()` e executa a simulação.

Os alertas e as cores seguem a tabela do enunciado. Trata-se de uma simulação didática, sem conexão com sensores.

## Exemplo de saída

```text
CONTROLE DE NÍVEIS DE ÁGUA
Simulação do reservatório

Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)

Simulação encerrada. Estilo padrão restaurado.
```

No terminal, as cinco linhas dos níveis aparecem nas respectivas cores.

## Verificação

```bash
python -m unittest -v
```

As verificações cobrem as cinco associações de nível, mensagem e cor, a restauração do estilo após cada alerta, a rejeição de níveis fora do intervalo e a execução dos cinco níveis na simulação.

## Arquivos

- `Guilherme_Gomes_Justi_Ag11_DSI_Recup.py`: programa principal.
- `requirements.txt`: dependência do projeto.
- `test_reservatorio.py`: verificações automatizadas.
- `.gitignore`: exclusão de arquivos temporários locais.

**Referência:** enunciado da atividade de recuperação da Agenda 11 - Controle de Níveis de Água, no ambiente EaDTEC, consultado em 09/11/2026.

