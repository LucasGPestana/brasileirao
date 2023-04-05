from partidas import *
import time as tempo

# Função para utilizar como chave na ordenação (sorted)
def ordenarPontos(time):
  return info_times[time]["Pontos"]

for rodada in range(1, 39, 1):

  info_times = gerar_rodada(rodada)

  ranking = sorted(info_times, key=ordenarPontos, reverse=True)
  
  tempo.sleep(5)
  print()
  
  with open(f"brasileirao/brasileirao/Rodadas/Rodada{rodada}(Classificação).txt", "a") as arquivo:
    for pos, time in enumerate(ranking):
      arquivo.write(f"{pos + 1} - {time} {info_times[time]}\n")
      print(f"{pos + 1} - {time} {info_times[time]}")
