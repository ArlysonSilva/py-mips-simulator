from memoria import ler_memoria, escrever_memoria

REGISTRADORES = {
    "$zero": 0, "$t0": 0, "$t1": 0, "$t2": 0, "$t3": 0,
    "$sp": 0x7ffffffc, "$ra": 0, "$pc": 0x00400000
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
    elif op == "lw":
        reg_dest, offset_base = args
        offset, base = offset_base.replace(")", "").split("(")
        endereco = REGISTRADORES[base] + int(offset)
        REGISTRADORES[reg_dest] = ler_memoria(endereco)
    elif op == "sw":
        reg_src, offset_base = args
        offset, base = offset_base.replace(")", "").split("(")
        endereco = REGISTRADORES[base] + int(offset)
        escrever_memoria(endereco, REGISTRADORES[reg_src])
    elif op == "beq":
        reg_a, reg_b, label = args
        if REGISTRADORES[reg_a] == REGISTRADORES[reg_b]:
            endereco = int(label, 0)
            REGISTRADORES["$pc"] = endereco
            return
    elif op == "j":
        endereco = int(args[0], 0)
        REGISTRADORES["$pc"] = endereco
        return

    REGISTRADORES["$pc"] += 4

def mostrar_estado(clock, instrucao):
    print(f"\n[Clock {clock}]")
    print(f"PC = {hex(REGISTRADORES['$pc'])}")
    print(f"Instrução: {instrucao['linha']}")
    print("Registradores:")
    for reg, val in REGISTRADORES.items():
        if reg != "$pc":
            print(f"  {reg}: {val}")
    print("Memória:")
    for addr, val in sorted(MEMORIA.items()):
        print(f"  {hex(addr)}: {val}")
