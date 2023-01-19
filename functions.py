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
        score_computer +=1
        return message
    elif opt_computer == "Papel":
      if opt_user == "Tijera":
        message = "Tijera le gana a Papel >> El Usuario ganó"
        score_user +=1
        return message
      else:
        message = "Papel le gana a Piedra >> El Computador ganó"
        score_computer +=1
        return message
    else:
      if opt_user == "Piedra":
        message = "Piedra le gana a Tijera >> El Usuario ganó"
        score_user +=1
        return message
      else:
        message = "Tijera le gana a Papel >> El Computador ganó"
        score_computer +=1
        return message
  
  
if __name__ == "__main__":
  opt_computer = computer_option()
  print("Computer: " + opt_computer)
  opt_user = computer_option()
  print("User: " + opt_user)
  su =0
  sc =0
  message = who_wins(opt_user, opt_computer, su, sc)
  print(message)
  