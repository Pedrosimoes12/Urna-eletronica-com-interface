import pickle
from typing import List
from common import *

class Urna():
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def votar(self):
        titulo_eleitor = int(input("Digite o titulo do eleitor: "))
        eleitor = self.get_eleitor(titulo_eleitor)

        if not eleitor:
            raise Exception("Eleitor não é desta Urna")

        print(eleitor)
        print("Pode votar!")
        print("===========")
        voto = int(input("Digite o numero do candidato: "))
        self.registrar_voto(eleitor, voto)

    def encerrar(self):
        with open(f'{self.__nome_arquivo}_final.pkl', 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        return info

def iniciar_urna(eleitores, candidatos):
    print("Iniciando Urna")
    print("==============")
    secao = int(input("Número da secao: "))
    zona = int(input("Número da zona: "))

    return Urna(secao, zona, candidatos, eleitores)

def carregar_votos(nome_arq):
    try:
        print("Carregando arquivo de candidatos ...")

        with open(nome_arq, 'rb') as arquivo:
            votos = pickle.load(arquivo)
            return votos
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")


