import tkinter as tk
from tkinter import messagebox

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro App")

        
        self.codigo_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.rua_var = tk.StringVar()
        self.bairro_var = tk.StringVar()
        self.cidade_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.cep_var = tk.StringVar()
        self.celular_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.cpf_var = tk.StringVar()
        self.rg_var = tk.StringVar()

        
        self.label_codigo = tk.Label(root, text="Código:")
        self.entry_codigo = tk.Entry(root, textvariable=self.codigo_var)

        self.label_nome = tk.Label(root, text="Nome:")
        self.entry_nome = tk.Entry(root, textvariable=self.nome_var)

        self.label_rua = tk.Label(root, text="Rua:")
        self.entry_rua = tk.Entry(root, textvariable=self.rua_var)

        self.label_bairro = tk.Label(root, text="Bairro:")
        self.entry_bairro = tk.Entry(root, textvariable=self.bairro_var)

        self.label_cidade = tk.Label(root, text="Cidade:")
        self.entry_cidade = tk.Entry(root, textvariable=self.cidade_var)

        self.label_estado = tk.Label(root, text="Estado:")
        self.entry_estado = tk.Entry(root, textvariable=self.estado_var)

        self.label_cep = tk.Label(root, text="CEP:")
        self.entry_cep = tk.Entry(root, textvariable=self.cep_var)

        self.label_celular = tk.Label(root, text="Celular:")
        self.entry_celular = tk.Entry(root, textvariable=self.celular_var)

        self.label_email = tk.Label(root, text="E-mail:")
        self.entry_email = tk.Entry(root, textvariable=self.email_var)

        self.label_cpf = tk.Label(root, text="CPF:")
        self.entry_cpf = tk.Entry(root, textvariable=self.cpf_var)

        self.label_rg = tk.Label(root, text="RG:")
        self.entry_rg = tk.Entry(root, textvariable=self.rg_var)

       
        self.save_button = tk.Button(root, text="Salvar", command=self.salvar_dados)

        
        self.label_codigo.grid(row=0, column=0, sticky="w")
        self.entry_codigo.grid(row=0, column=1)

        self.label_nome.grid(row=1, column=0, sticky="w")
        self.entry_nome.grid(row=1, column=1)

        self.label_rua.grid(row=2, column=0, sticky="w")
        self.entry_rua.grid(row=2, column=1)

        self.label_bairro.grid(row=3, column=0, sticky="w")
        self.entry_bairro.grid(row=3, column=1)

        self.label_cidade.grid(row=4, column=0, sticky="w")
        self.entry_cidade.grid(row=4, column=1)

        self.label_estado.grid(row=5, column=0, sticky="w")
        self.entry_estado.grid(row=5, column=1)

        self.label_cep.grid(row=6, column=0, sticky="w")
        self.entry_cep.grid(row=6, column=1)

        self.label_celular.grid(row=7, column=0, sticky="w")
        self.entry_celular.grid(row=7, column=1)

        self.label_email.grid(row=8, column=0, sticky="w")
        self.entry_email.grid(row=8, column=1)

        self.label_cpf.grid(row=9, column=0, sticky="w")
        self.entry_cpf.grid(row=9, column=1)

        self.label_rg.grid(row=10, column=0, sticky="w")
        self.entry_rg.grid(row=10, column=1)

        self.save_button.grid(row=11, column=0, columnspan=2)

    def salvar_dados(self):
        
        codigo = self.codigo_var.get()
        nome = self.nome_var.get()
        rua = self.rua_var.get()
        bairro = self.bairro_var.get()
        cidade = self.cidade_var.get()
        estado = self.estado_var.get()
        cep = self.cep_var.get()
        celular = self.celular_var.get()
        email = self.email_var.get()
        cpf = self.cpf_var.get()
        rg = self.rg_var.get()

        
        dados = f"Código: {codigo}\nNome: {nome}\nRua: {rua}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}\nCEP: {cep}\nCelular: {celular}\nE-mail: {email}\nCPF: {cpf}\nRG: {rg}"

        try:
            
            with open("dados.txt", "a") as file:
                file.write("\n\n" + dados)
                messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar os dados: {str(e)}")


root = tk.Tk()
app = CadastroApp(root)


root.mainloop()
