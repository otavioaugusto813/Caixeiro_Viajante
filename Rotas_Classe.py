import googlemaps
from Embaralhar import embaralhar_lista
from itertools import permutations
import datetime

gmaps = googlemaps.Client(key = 'your-key')

class Rotas:

    def __init__(self, origem:str, lista_cidades:list):
        self.origem = origem
        self.lista_cidades = lista_cidades

    def calcular_rotas(self):
        """Função principal que calcula, de fato, todas as possibilidades de rotas e retorna aquela cujo tempo total somado seja menor"""
        local = self.lista_cidades[:]
        trajetos = []
        trajetos.append(local[:])
        tempo = []
        viagem = []
        viagem_final = {}
        n_permut = len (list (map (", ".join, permutations(self.lista_cidades))))
        i = 0

        if len (self.lista_cidades) < 6:
            while i <= (n_permut - 1):
                viagem.clear ()
                tempo.clear ()
                origem1 = self.origem[:]
                origem2 = self.origem[:]

                for destino in local:
                    ida = gmaps.distance_matrix (f'City of {origem2}, State of Minas Gerais, Brazil',
                                                 f'City of {destino}, State of Minas Gerais, Brazil')
                    viagem.append (ida)  # adicionando todas as informações da ida
                    tempo.append (ida['rows'][0]['elements'][0]['duration']['value'])  # adicionando apenas o tempo
                    origem2 = destino

                    if destino == local[-1]:
                        volta = gmaps.distance_matrix (f'City of {local[-1]}, State of Minas Gerais, Brazil',
                                                       f'City of {origem1}, State of Minas Gerais, Brazil')  # calculando a volta a partir do último destino
                        viagem.append (volta)  # adicionando as informações da volta
                        tempo_volta = volta['rows'][0]['elements'][0]['duration']['value']
                        tempo.append (tempo_volta)  # adicionando o tempo da volta


                        x = f"{origem1} > " + ' > '.join (trajetos[i]) + f" > {origem1}"
                        viagem_final[f'{x}'] = sum (tempo[:])

                embaralhar_lista(local, trajetos)
                i += 1

            minimo = min (viagem_final, key=viagem_final.get)
            horas = str (datetime.timedelta (seconds=viagem_final[minimo]))
            resultado = f'O trajeto mais rápido é {minimo}, com uma duração de {horas} horas.'
            return resultado

        else:
            return 'Algoritmo O(n!) e , por isso, o número máximo de cidades é 5.'
