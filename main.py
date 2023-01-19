import functions
import sys

options = ("Piedra", "Papel", "Tijera")
print(">> Bienvenido al juego de Piedra, Papel o Tijera")
nickname = input("Elige un nickname para jugar => ")
games = input("Elige con cuantas partidas ganadas se termina el juego => ")

if not games.isnumeric():
  print(f"Elegiste {games} y este no es un valor válido. Debes escoger un número.")
  sys.exit()
else:
  games = int(games)
  score_user = 0
  score_computer =0
  round = 1
  
  while score_computer<games and score_user<games:
    print(f"\n >>> Ronda {round} ")
    opt_user = input("Escoja una opción >> ").capitalize()
    if opt_user in options:
      opt_computer = functions.computer_option(options)
      message, score_user, score_computer = functions.who_wins(opt_user, opt_computer, score_user, score_computer)
      print(f"El Computador escogío {opt_computer}")
      print(message)
      print(f"Marcador: {nickname} {score_user} y Computer {score_computer} ")
      round += 1
      continue
    else:
      print("Opción no válida")
      print("Intentelo de nuevo")
      continue

  print(f"\nFinalmente luego de {round} rounds ...")
  functions.champion(score_user, score_computer, nickname)
  
