from calendar import c
import tkinter as tk

def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('Janela Nova')
    botao_fechar = tk.Button(janela2, text="fechar", command=janela2.destroy)
    botao_fechar.grid(row=1, column=0)

janela = tk.Tk()
botao = tk.Button(janela, text="Ir para outra janela", command=abrir_janela)
botao.grid(row=2, column=3)

janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

janela.mainloop()