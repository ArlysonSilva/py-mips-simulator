addi $t0, $zero, 5
addi $t1, $zero, 10
add  $t2, $t0, $t1
sw $t2, 0($sp)
lw $t3, 0($sp)
beq $t3, $t2, 0x00400000
