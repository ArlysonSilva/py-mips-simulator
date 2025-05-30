def tipo_instrucao(opcode):
    if opcode in ["add", "sub", "and", "or", "slt"]:
        return "R"
    elif opcode in ["addi", "lw", "sw", "beq", "bne"]:
        return "I"
    elif opcode in ["j", "jal"]:
        return "J"
    return "Desconhecido"

def ler_instrucoes(arquivo):
    instrucoes = []
    with open(arquivo, "r") as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith("#"):
                continue  # Ignorar linhas vazias ou comentários
            partes = linha.replace(",", "").split()
            opcode = partes[0]
            args = partes[1:]
            instrucoes.append({
                "linha": linha,
                "opcode": opcode,
                "args": args,
                "tipo": tipo_instrucao(opcode)
            })
    return instrucoes
