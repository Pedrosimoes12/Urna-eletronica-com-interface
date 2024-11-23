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
        print("O arquivo votos.pkl está vazio.")
        return []

# Carregar e exibir os votos
votos = carregar_votos()
if votos:
    for i, voto in enumerate(votos, start=1):
        print(f"Voto {i}: {voto}")
else:
    print("Nenhum voto registrado.")