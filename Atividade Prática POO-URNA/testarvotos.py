import pickle

# Função para carregar votos do arquivo .pkl
def carregar_votos():
    try:
        with open('votos.pkl', 'rb') as arquivo:
            votos = pickle.load(arquivo)
            return votos
    except FileNotFoundError:
        print("O arquivo votos.pkl não foi encontrado.")
        return []
    except EOFError:
        return []

# Carregar e exibir os votos
votos = carregar_votos()
if votos:
    for i, voto in enumerate(votos, start=0):
        if i > 0:
            print(f"Voto {i}: {voto}")