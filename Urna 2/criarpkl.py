import pickle
candidatos = [{"nome": "Ferauche", "numero": 33}, {"nome": "Joao", "numero": 77}, {"nome": "Apolinario", "numero": 48}, {"nome": "Moreira", "numero": 80},
              {"nome": "Walter", "numero": 10}, {"nome": "Kuribara", "numero": 50}, {"nome": "Stucchi", "numero": 66}, {"nome": "Ronaldo", "numero": 20}]

eleitores = [{"nome": "Pedro", "titulo": "1"}, {"nome": "Mateus", "titulo": "2"}, {"nome": "Gabriela", "titulo": "3"},
             {"nome": "Vitor", "titulo": "4"}, {"nome": "Felipe", "titulo": "5"}]

with open('candidatos.pkl', 'wb') as f:
    pickle.dump(candidatos, f)

with open('eleitores.pkl', 'wb') as f:
    pickle.dump(eleitores, f)