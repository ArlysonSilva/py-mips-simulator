MEMORIA = {}

def ler_memoria(endereco):
    return MEMORIA.get(endereco, 0)

def escrever_memoria(endereco, valor):
    MEMORIA[endereco] = valor
