def carregar_programa(caminho):
    programa = []
    with open(caminho, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha == "" or linha.startswith("#"):
                continue
            partes = linha.split()
            opcode = partes[0]
            args = linha[len(opcode):].strip().split(",")
            args = [arg.strip() for arg in args]
            programa.append({"opcode": opcode, "args": args, "linha": linha})
    return programa
