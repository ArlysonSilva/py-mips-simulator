MEMORIA = {}

REGISTRADORES = {
    "$zero": 0, "$t0": 0, "$t1": 0, "$t2": 0, "$t3": 0,
    "$sp": 0, "$ra": 0, "$pc": 0x00400000
}

class CPU:
    def __init__(self):
        self.resetar()

    def resetar(self):
        global REGISTRADORES, MEMORIA
        for reg in REGISTRADORES:
            REGISTRADORES[reg] = 0
        REGISTRADORES["$pc"] = 0x00400000
        MEMORIA.clear()
        self.ciclo = 0

    def executar(self, instrucao):
        self.ciclo += 1
        op = instrucao["opcode"]
        args = instrucao["args"]

        if op == "addi":
            reg_dest, reg_src, imediato = args
            REGISTRADORES[reg_dest] = REGISTRADORES[reg_src] + int(imediato)
        elif op == "add":
            reg_dest, reg_a, reg_b = args
            REGISTRADORES[reg_dest] = REGISTRADORES[reg_a] + REGISTRADORES[reg_b]
        elif op == "sw":
            reg_val, desloc, reg_base = args
            endereco = REGISTRADORES[reg_base] + int(desloc)
            MEMORIA[endereco] = REGISTRADORES[reg_val]
        elif op == "lw":
            reg_dest, desloc, reg_base = args
            endereco = REGISTRADORES[reg_base] + int(desloc)
            REGISTRADORES[reg_dest] = MEMORIA.get(endereco, 0)
        elif op == "beq":
            reg_a, reg_b, endereco = args
            if REGISTRADORES[reg_a] == REGISTRADORES[reg_b]:
                REGISTRADORES["$pc"] = int(endereco, 0)
                return  # salto, não incrementa PC abaixo
        elif op == "j":
            endereco = int(args[0], 0)
            REGISTRADORES["$pc"] = endereco
            return

        REGISTRADORES["$pc"] += 4

    def mostrar_estado(self):
        estado = []
        estado.append(f"[Clock {self.ciclo}] PC = {hex(REGISTRADORES['$pc'])}")
        for reg, val in REGISTRADORES.items():
            if reg != "$pc":
                estado.append(f"{reg}: {val}")
        return "\n".join(estado)
