import tkinter as tk
class veterinario:
    def __init__(self,nome,email,endereço,__senha):
        self.nome=nome
        self.email=email
        self.endereço=endereço
        self.__senha=__senha
        self.agenda=[]
def mostrar():
    nome_veterinario=nome.get()
    email_veterinario=email.get()
    veterinario_cadastrado=veterinario(nome_veterinario,email_veterinario,"sssxss","vvvvvvvv")
    terminar_cadstro=tk.Label(text=veterinario_cadastrado.nome)
    terminar_cadstro.grid(column=2,row=3)

janela=tk.Tk()
janela.geometry("1050x520")

cadastro_nome=tk.Label(text="Qual o nome do veterinario")
cadastro_nome.grid(column=1,row=1)
nome=tk.Entry()
nome.grid(column=1,row=2)

cadastro_email=tk.Label(text="Qual o email do veterinario")
cadastro_email.grid(column=1,row=3)
email=tk.Entry()
email.grid(column=1,row=4)

cadastro_endereço=tk.Label(text="Qual o endereço do veterinario")
cadastro_endereço.grid(column=1,row=5)
endereço=tk.Entry()
endereço.grid(column=1,row=6)

cadastro_endereço=tk.Label(text="Qual o codigo do veterinario")
cadastro_endereço.grid(column=1,row=7)
endereço=tk.Entry()
endereço.grid(column=1,row=8)

botao=tk.Button(text="finalizar",command=mostrar)
botao.grid(column=2,row=9)
janela.mainloop()
