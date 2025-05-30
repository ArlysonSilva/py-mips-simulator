from parser import carregar_programa
from cpu import CPU

# Registradores com PC inicializado
REGISTRADORES = {
    "$zero": 0, "$t0": 0, "$t1": 0, "$t2": 0, "$t3": 0,
    "$sp": 0, "$ra": 0, "$pc": 0x00400000  # PC inicia aqui
}

def ler_configuracao():
    configuracoes = {}
    with open("config.txt", "r") as arquivo:
        for linha in arquivo:
            if linha.strip() and not linha.startswith("#"):
                chave, valor = linha.strip().split("=")
                configuracoes[chave.strip()] = int(valor.strip())
    return configuracoes

def instrucao_para_binario(instrucao):
    # Placeholder: aqui você pode implementar a conversão real para MIPS binário
    # Por hora, apenas retorno uma string informativa
    return "binário simulado (implemente depois)"

def mostrar_estado(clock, instrucao):
    print(f"\n[Clock {clock}]")
    print(f"PC = {hex(REGISTRADORES['$pc'])}")
    print(f"Instrução: {instrucao['linha']}")
    print(f"Instrução binária: {instrucao_para_binario(instrucao)}")
    print(f"Instrução hexadecimal: {hex(REGISTRADORES['$pc'])}")
    for reg, val in REGISTRADORES.items():
        if reg != "$pc":
            print(f"{reg}: {val}")

def main():
    config = ler_configuracao()
    clock_mhz = config.get("clock_mhz", 1000)
    tipo_i = config.get("tipo_i", 0)
    tipo_r = config.get("tipo_r", 0)
    tipo_j = config.get("tipo_j", 0)

    cpu = CPU()
    programa = carregar_programa("exemplos/programa.asm")
    ciclo = 1
    for instrucao in programa:
        cpu.executar(instrucao)
        mostrar_estado(ciclo, instrucao)
        ciclo += 1

    tempo_total_ns = ciclo * (1 / (clock_mhz * 10**6)) * 1e9
    print(f"\nExecução concluída em {ciclo} ciclos.")
    print(f"Tempo total de execução: {tempo_total_ns:.2f} ns")
    print(f"Ciclos: {ciclo}, Clock: {clock_mhz} MHz")

if __name__ == "__main__":
    main()
