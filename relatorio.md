# Relatório do Simulador MIPS

## Objetivo
Criar um simulador funcional de MIPS em Python, capaz de ler, interpretar e executar instruções do tipo R, I e J.

## Funcionalidades implementadas
- Leitura do arquivo `.asm` com instruções MIPS
- Identificação do tipo da instrução (R, I ou J)
- Simulação de registradores (incluindo PC)
- Simulação de memória
- Instruções implementadas: addi, add, j, lw, sw, beq
- Exibição do estado da CPU e memória a cada ciclo

## Como usar
1. Edite `exemplos/programa.asm` para incluir instruções MIPS.
2. Rode `python main.py` para executar a simulação.

## Extensões futuras
- Adicionar mais instruções (sub, and, or, slt, bne)
- Implementar contagem de ciclos realista
- Interface gráfica com tkinter
