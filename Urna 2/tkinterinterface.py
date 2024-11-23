import tkinter as tk
from tkinter import messagebox
from urna import UrnaEletronica


class UrnaInterface:
    def __init__(self, root):
        self.urna = UrnaEletronica()
        self.root = root
        self.root.title("Urna Eletrônica")

        # Entrada do titulo de eleitor
        tk.Label(root, text="Digite o título do eleitor:").pack(pady=10)
        self.entrada_titulo = tk.Entry(root)
        self.entrada_titulo.pack(pady=5)
        tk.Button(root, text="Buscar Eleitor", command=self.buscar_eleitor).pack(pady=10)

    def buscar_eleitor(self):
        titulo = self.entrada_titulo.get()
        eleitor = self.urna.buscar_eleitor(titulo)
        if eleitor:
            if self.urna.ja_votou(titulo):
                messagebox.showwarning("Aviso", "Este eleitor já votou.")
            else:
                self.iniciar_votacao(eleitor)
        else:
            messagebox.showerror("Erro", "Eleitor não encontrado.")

    def iniciar_votacao(self, eleitor):
        # Criação de nova janela para votação
        janela_voto = tk.Toplevel(self.root)
        janela_voto.title("Teclado Virtual")

        # Funções de manipulação do teclado
        def inserir_numero(num):
            entrada_numero.insert(tk.END, num)
            atualizar_nome_candidato()

        def corrige():
            entrada_numero.delete(0, tk.END)
            label_candidato['text'] = ""

        def branco():
            registrar_voto("Branco")

        def confirma():
            numero = entrada_numero.get()
            voto = self.urna.processar_voto(numero)
            registrar_voto(voto)

        def registrar_voto(voto):
            self.urna.salvar_voto(eleitor['titulo'], voto)
            messagebox.showinfo("Voto registrado", f"Voto em '{voto}' computado com sucesso.")
            janela_voto.destroy()

        def atualizar_nome_candidato():
            numero = entrada_numero.get()
            nome = self.urna.get_nome_candidato(numero)
            label_candidato['text'] = nome

        # Escrita da janela de votação
        entrada_numero = tk.Entry(janela_voto, font=("Arial", 24), justify='center')
        entrada_numero.grid(row=0, column=0, columnspan=3, pady=10)

        label_candidato = tk.Label(janela_voto, text="", font=("Arial", 18), fg="blue")
        label_candidato.grid(row=1, column=0, columnspan=3, pady=5)

        # Teclado para votar
        botoes = [
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
            ('0', 5, 1)
        ]
        for (text, row, col) in botoes:
            tk.Button(janela_voto, text=text, font=("Arial", 18), width=5, height=2,
                      command=lambda t=text: inserir_numero(t)).grid(row=row, column=col)

        # Botões de decisão
        tk.Button(janela_voto, text="BRANCO", bg="white", width=10, height=2, command=branco).grid(row=6, column=0,
                                                                                                   pady=5)
        tk.Button(janela_voto, text="CORRIGE", bg="orange", width=10, height=2, command=corrige).grid(row=6, column=1,
                                                                                                      pady=5)
        tk.Button(janela_voto, text="CONFIRMA", bg="green", width=10, height=2, command=confirma).grid(row=6, column=2,
                                                                                                       pady=5)


# Iniciar interface da urna
if __name__ == "__main__":
    root = tk.Tk()
    app = UrnaInterface(root)
    root.mainloop()