import random

def computer_option():
  options = ("Piedra", "Papel", "Tijera")
  option_choose = random.choice(options)
  return option_choose


  
if __name__ == "__main__":
  opt = computer_option()
  print(opt)