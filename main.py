from parser import ler_instrucoes
from cpu import REGISTRADORES, executar, mostrar_estado
# Simulador de registradores
REGISTRADORES = {
    "$zero": 0, "$t0": 0, "$t1": 0, "$t2": 0, "$t3": 0,
    "$sp": 0, "$ra": 0, "$pc": 0x00400000  # PC inicia aqui
}

def executar(instrucao):
    op = instrucao["opcode"]
    args = instrucao["args"]

    if op == "addi":
        reg_dest, reg_src, imediato = args
        REGISTRADORES[reg_dest] = REGISTRADORES[reg_src] + int(imediato)
    elif op == "add":
        reg_dest, reg_a, reg_b = args
        REGISTRADORES[reg_dest] = REGISTRADORES[reg_a] + REGISTRADORES[reg_b]
    elif op == "j":
        endereco = int(args[0], 0)  # interpretando como hexadecimal
        REGISTRADORES["$pc"] = endereco
        return  # simula salto

    # Incrementa PC para próxima instrução
    REGISTRADORES["$pc"] += 4

def mostrar_estado(clock, instrucao):
    print(f"\n[Clock {clock}]")
    print(f"PC = {hex(REGISTRADORES['$pc'])}")
    print(f"Instrução: {instrucao['linha']}")
    for reg, val in REGISTRADORES.items():
        if reg != "$pc":
            print(f"{reg}: {val}")

def main():
    instrucoes = ler_instrucoes("exemplos/programa.asm")
    clock = 1
    i = 0
    while i < len(instrucoes):
        instrucao = instrucoes[i]
        executar(instrucao)
        mostrar_estado(clock, instrucao)

        if instrucao["opcode"] in ["j", "beq"]:
            endereco = REGISTRADORES["$pc"]
            i = (endereco - 0x00400000) // 4
        else:
            i += 1

        clock += 1

if __name__ == "__main__":
    main()
