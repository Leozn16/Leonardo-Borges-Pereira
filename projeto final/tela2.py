import tkinter as tk
from tkinter import ttk
janela=tk.Tk()
janela.title("index/agenda")
cabeçario=tk.Label(text="clinica veterinaria")
cabeçario.grid(column=1,row=1,columnspan=9)


#veterinarios=["azul","vermelho","amarelo"]
#veterinarios=ttk.Combobox(janela,values=veterinarios)
#veterinarios.grid(column=1,row=2) 

#veterinarios=["azul vermelhado","vermelho amarelado","amarelo azulado"]
#veterinarios=ttk.Combobox(janela,values=veterinarios)
#veterinarios.grid(column=1,row=2) 

botao = tk.Button(text="azul")
botao.grid(row=2, column=1)

botao = tk.Button(text="vermelho")
botao.grid(row=3, column=1)

botao = tk.Button(text="amarelo")
botao.grid(row=4, column=1,)






janela.mainloop()