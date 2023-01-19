import random

def computer_option():
  options = ("Piedra", "Papel", "Tijera")
  option_choose = random.choice(options)
  return option_choose

def who_wins(opt_user, opt_computer, score_user, score_computer):
  if opt_computer == opt_user:
    message = "Hubo un empate"
    return message
  else:
    if opt_computer == "Piedra":
      if opt_user == "Papel":
        message = "Papel le gana a piedra >> El Usuario ganó"
        score_user +=1
        return message
      else:
        message = "Piedra le gana a Tijera >> El Computador ganó"
        score_user +=1
        return message
    elif opt_computer == "Papel":
      if opt_user == "Papel":
        
  
if __name__ == "__main__":
  opt = computer_option()
  print(opt)