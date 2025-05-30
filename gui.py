import tkinter as tk
from tkinter import filedialog, messagebox
from cpu import CPU
from parser import carregar_programa

class SimuladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador MIPS")

        self.programa = []
        self.cpu = CPU()

        self.area_programa = tk.Text(root, height=15, width=60)
        self.area_programa.pack()

        self.area_estado = tk.Text(root, height=15, width=60)
        self.area_estado.pack()

        frame_botoes = tk.Frame(root)
        frame_botoes.pack()

        self.botao_carregar = tk.Button(frame_botoes, text="Carregar Arquivo", command=self.carregar_programa)
        self.botao_carregar.pack(side=tk.LEFT, padx=5, pady=5)

        self.botao_executar = tk.Button(frame_botoes, text="Executar", command=self.executar_programa)
        self.botao_executar.pack(side=tk.LEFT, padx=5, pady=5)

        self.botao_proximo = tk.Button(frame_botoes, text="Próximo Ciclo", command=self.proximo_ciclo)
        self.botao_proximo.pack(side=tk.LEFT, padx=5, pady=5)

        self.botao_reiniciar = tk.Button(frame_botoes, text="Reiniciar", command=self.reiniciar)
        self.botao_reiniciar.pack(side=tk.LEFT, padx=5, pady=5)

        self.indice_instrucao = 0

    def carregar_programa(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivo ASM", "*.asm"), ("Todos os arquivos", "*.*")])
        if caminho:
            self.programa = carregar_programa(caminho)
            self.area_programa.delete(1.0, tk.END)
            for instrucao in self.programa:
                self.area_programa.insert(tk.END, f"{instrucao['linha']}\n")
            self.reiniciar()

    def executar_programa(self):
        if not self.programa:
            messagebox.showwarning("Aviso", "Nenhum programa carregado!")
            return
        self.reiniciar()
        for instrucao in self.programa:
            self.cpu.executar(instrucao)
            self.area_estado.insert(tk.END, self.cpu.mostrar_estado() + "\n\n")
        messagebox.showinfo("Execução", "Execução concluída!")

    def proximo_ciclo(self):
        if self.indice_instrucao < len(self.programa):
            instrucao = self.programa[self.indice_instrucao]
            self.cpu.executar(instrucao)
            self.area_estado.insert(tk.END, self.cpu.mostrar_estado() + "\n\n")
            self.indice_instrucao += 1
        else:
            messagebox.showinfo("Fim", "Programa finalizado!")

    def reiniciar(self):
        self.cpu.resetar()
        self.area_estado.delete(1.0, tk.END)
        self.indice_instrucao = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorGUI(root)
    root.mainloop()
