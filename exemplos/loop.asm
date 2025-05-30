# Inicializa registradores
addi $t0, $zero, 10      # $t0 = 10 (contador)
addi $t1, $zero, 0       # $t1 = 0 (acumulador)

loop:
    add  $t1, $t1, $t0   # $t1 += $t0
    addi $t0, $t0, -1    # $t0 -= 1
    beq  $t0, $zero, end # se $t0 == 0, pula para end
    j    loop            # senão, repete o loop

end:
    sw   $t1, 0($sp)     # salva resultado na memória
    lw   $t2, 0($sp)     # carrega resultado em $t2
