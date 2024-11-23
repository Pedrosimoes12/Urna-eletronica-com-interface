import pickle

class UrnaEletronica:
    def __init__(self):
        self.candidatos = self.carregar_arquivo('candidatos.pkl')
        self.eleitores = self.carregar_arquivo('eleitores.pkl')
        self.eleitores_votaram = set()

    def carregar_arquivo(self, nome_arquivo):
        if nome_arquivo:
            with open(nome_arquivo, 'rb') as arquivo:
                return pickle.load(arquivo)
        else:
            return "Erro, arquivo não encontrado"

    def buscar_eleitor(self, titulo):
        return next((e for e in self.eleitores if e['titulo'] == titulo), None)

    def ja_votou(self, titulo):
        return titulo in self.eleitores_votaram

    def processar_voto(self, numero):
        if not numero:
            return "Branco"
        for c in self.candidatos:
            if str(c['numero']) == numero:
                return c['nome']
        return "Nulo"

    def salvar_voto(self, titulo, voto):
        votos = self.carregar_arquivo('votos.pkl')
        votos.append({"titulo": titulo, "voto": voto})
        with open('votos.pkl', 'wb') as arquivo:
            pickle.dump(votos, arquivo)
        self.eleitores_votaram.add(titulo)

    def get_nome_candidato(self, numero):
        for c in self.candidatos:
            if str(c['numero']) == numero:
                return f"Candidato: {c['nome']}"
        return "Número inválido" if numero else ""