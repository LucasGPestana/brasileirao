from times import *
import random
import time as tempo
   
def info_gols(time_info, gols_marcados, gols_sofridos):
   
   times[time_info]["Gols Marcados"] += gols_marcados
   times[time_info]["Gols Sofridos"] += gols_sofridos
   times[time_info]["Saldo de Gols"] += (gols_marcados - gols_sofridos)

# While True repete o sorteio até que os times sejam diferentes
def gerar_rodada(rodada):

  partidas = []

  times_nao_jogaram = []

  for time in times:
     times_nao_jogaram.append(time)

  times_jogaram = []
  numero_partida = 0

  with open(f"brasileirao/brasileirao/Rodadas/Rodada{rodada}(Partidas).txt", "a") as arquivo:
     arquivo.write(f"Rodada {rodada}\n")
  print(f"Rodada {rodada}")

  random.shuffle(times_nao_jogaram)

  while numero_partida < 10:

      while True:

        time1 = random.choice(times_nao_jogaram)
        time2 = random.choice(times_nao_jogaram)

        if time1 == time2:
          continue
        else:
          break

      times_nao_jogaram.remove(time1)
      times_nao_jogaram.remove(time2)

      times_jogaram.append(time1)
      times_jogaram.append(time2)

      with open(f"brasileirao/brasileirao/Rodadas/Rodada{rodada}(Partidas).txt", "a") as arquivo:
         arquivo.write(f"{numero_partida + 1} - {time1} x {time2}\n")

      print(f"{numero_partida + 1} - {time1} x {time2}")

      partidas.append({time1: 0, time2: 0})

      numero_partida += 1

  # Gera um placar aleatório às partidas da rodada  
  for partida in partidas:
    for time in partida:
        partida[time] = random.randint(0, 5)

  # Adicionar as informações ao dicionário times
  # Compara se os times são diferentes e se o placar de um é maior que o do outro
  # O break serve para evitar contagens múltiplas

  for partida in partidas:
    for time in partida:
        for time2 in partida:
          if time != time2 and partida[time] > partida[time2]:
              
              times[time]["Vitórias"] += 1
              times[time]["Pontos"] += 3
              info_gols(time, partida[time], partida[time2])
              
              times[time2]["Derrotas"] += 1
              info_gols(time2, partida[time2], partida[time])

              break
          
          elif time != time2 and partida[time] == partida[time2]:
              
              times[time]["Empates"] += 1
              times[time]["Pontos"] += 1
              info_gols(time, partida[time], partida[time2])

              times[time2]["Empates"] += 1
              times[time]["Pontos"] += 1
              info_gols(time2, partida[time2], partida[time])

              break
          
          else:
              continue

  tempo.sleep(5)
  print()

  # Mostra o placar de cada partida
  # O número do time serve para identificar qual é o primeiro time e qual o segundo
  with open(f"brasileirao/brasileirao/Rodadas/Rodada{rodada}(Partidas).txt", "a") as arquivo:
    arquivo.write("\n")
    for numero, partida in enumerate(partidas):
      arquivo.write(f"{numero + 1} - ")
      print(f"{numero + 1} - ", end="")
      for numero_time, time in enumerate(partida):
          if numero_time == 0:
            arquivo.write(f"{time} {partida[time]} x ")
            print(f"{time} {partida[time]} x ", end="")
          else:
            arquivo.write(f"{time} {partida[time]}\n")
            print(f"{time} {partida[time]}")
  
  return times