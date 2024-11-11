from tkinter import *

# classe da internet pra teste e aprendizado do tkinter
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.criarBotoes()
        self.criarLabels()
        self.entradaDados()

    def criarBotoes(self):
        self.botao = Button(self)
        self.botao['text'] = 'Bem vindo ao Python'
        self.botao['fg'] = 'red'
        self.botao['bg'] = 'yellow'
        self.botao.pack(side='top')

        # segunda forma de criar botões
        self.botao1 = Button(self, text='Segundo botão', fg='blue', bg='red')
        self.botao1.pack(side='top')

    def criarLabels(self):
        self.label = Label(self)
        self.label['text'] = 'Bem vindo ao Python'
        self.label.pack(side='top')

    def entradaDados(self):
        self.edit = Entry(self)
        self.edit.pack(side='top')

minhaAplicacao = App()

minhaAplicacao.master.title('videoaulas Neri')
minhaAplicacao.master.maxsize(1024, 768)

minhaAplicacao.mainloop()
