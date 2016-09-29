'''this program mimics the game of rock-paper-scissors. rules for this game can be found here: https://youtu.be/E7OCzz_XuiI'''

from random import randint
from time import sleep

options = ["R", "P", "S"]
lose = "Oh, the crushing feeling of defeat."
win = "Congratulations, victory is yours."

def decide_winner(user_choice, cpu_choice):
  print "You have chosen %s." % user_choice
  print
  sleep(1)
  print "Computer selecting..."
  sleep(1)
  print
  print "Le computer has chosen %s." % cpu_choice
  print
  user_choice_index = options.index(user_choice)
  cpu_choice_index = options.index(cpu_choice)
  if user_choice == cpu_choice:
    print "It's a tie."
  elif user_choice_index == 0 and cpu_choice_index == 2:
    print win
  elif user_choice_index == 1 and cpu_choice_index == 0:
    print win
  elif user_choice_index == 2 and cpu_choice_index == 1:
    print win
  elif user_choice_index > 2:
    print "you have chosen an invalid option"
    return
  else:
    print lose
    return
  print

def play_RPS():
  print
  print "Rock, paper or scissors?"
  print
  user_choice = raw_input("Select R for rock, P for paper, or S for scissors: ")
  user_choice = user_choice.upper()
  print
  sleep(1)
  cpu_choice = options[randint(0,len(options)-1)]
  print
  decide_winner(user_choice, cpu_choice)

play_RPS()