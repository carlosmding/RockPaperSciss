import functions

options = ("Piedra", "Papel", "Tijera")
print(">> Bienvenido al juego de Piedra, Papel o Tijera")
nickname = input("Escoge un nickname para jugar => ")
print(f"{nickname} empecemos")

score_user = 0
score_computer =0
round = 1

while score_computer <2 and score_user <2:
  
  print(f"\n >>> Ronda {round} ")
  opt_user = input("Escoja una opción >> ")
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
  