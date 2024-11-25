
import tkinter as tk
from tkinter import messagebox
from urna import UrnaEletronica
from criarpkl import criar_votos


class UrnaInterface:
    def __init__(self, root):
        self.urna = UrnaEletronica()
        self.root = root
        self.root.title("Urna Eletrônica")

        # Entrada do título de eleitor
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
                self.mostrar_dados_eleitor(eleitor)
        else:
            messagebox.showerror("Erro", "Eleitor não encontrado.")

    def mostrar_dados_eleitor(self, eleitor):
        # Criação de uma nova janela para exibir os dados do eleitor
        janela_dados = tk.Toplevel(self.root)
        janela_dados.title("Dados do Eleitor")

        # Exibir os dados do eleitor
        tk.Label(janela_dados, text="Dados do Eleitor", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(janela_dados, text=f"Nome: {eleitor['nome']}").pack(pady=5)
        tk.Label(janela_dados, text=f"Título: {eleitor['titulo']}").pack(pady=5)

        # Botão para iniciar a votação
        tk.Button(janela_dados, text="Iniciar Votação", bg="green", fg="white", command=lambda: self.iniciar_votacao(eleitor)).pack(pady=20)
        # Botão para cancelar
        tk.Button(janela_dados, text="Cancelar", bg="red", fg="white", command=janela_dados.destroy).pack(pady=5)

    def iniciar_votacao(self, eleitor):
        # Fecha a janela de dados do eleitor
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel) and widget.title() == "Dados do Eleitor":
                widget.destroy()

        # Criação de nova janela para votação (implementação já explicada)
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
            if not numero:  # Verifica se não digitou nenhum numero antes de confirmar
                registrar_voto("Nulo")
            else:
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

        # Configuração da entrada e informações ao lado do teclado
        entrada_frame = tk.Frame(janela_voto)
        entrada_frame.grid(row=0, column=0, padx=20, pady=10)

        entrada_numero = tk.Entry(entrada_frame, font=("Arial", 24), justify='center', width=10)
        entrada_numero.pack(pady=10)

        label_candidato = tk.Label(entrada_frame, text="", font=("Arial", 18), fg="blue", wraplength=200)
        label_candidato.pack(pady=10)

        # Configuração do teclado
        teclado_frame = tk.Frame(janela_voto)
        teclado_frame.grid(row=0, column=1, padx=20, pady=10)

        botoes = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('0', 3, 1)
        ]
        for (text, row, col) in botoes:
            tk.Button(teclado_frame, text=text, font=("Arial", 18), width=5, height=2,
                      command=lambda t=text: inserir_numero(t)).grid(row=row, column=col, padx=5, pady=5)

        # Botões de decisão abaixo do teclado
        tk.Button(teclado_frame, text="BRANCO", bg="white", width=10, height=2, command=branco).grid(row=4, column=0,
                                                                                                    pady=10)
        tk.Button(teclado_frame, text="CORRIGE", bg="orange", width=10, height=2, command=corrige).grid(row=4, column=1,
                                                                                                       pady=10)
        tk.Button(teclado_frame, text="CONFIRMA", bg="green", width=10, height=2, command=confirma).grid(row=4, column=2,
                                                                                                        pady=10)


# Iniciar interface da urna
if __name__ == "__main__":
    criar_votos()
    root = tk.Tk()
    app = UrnaInterface(root)
    root.mainloop()
