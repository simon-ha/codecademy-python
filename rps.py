'''this program mimics the game of rock-paper-scissors. rules for this game can be found here: https://youtu.be/E7OCzz_XuiI'''

from random import randint
from time import sleep

options = ["R", "P", "S"]
lose = "Oh, the crushing feeling of defeat."
win = "Congratulations, victory is yours."

# defining the function that decides the winner. splitting off from play_RPS below.
# this is executed after play_RPS, but comes first as it decide_winner must be defined 
def decide_winner(user_choice, cpu_choice):
  print "You have chosen %s." % user_choice # don't worry, this is defined below
  print
  sleep(1)
  print "Computer selecting..."
  print
  print "Le computer chose %s." % cpu_choice
  print
  user_choice_index = options.index(user_choice) # this is a new fxn. need to digest
  cpu_choice_index = options.index(cpu_choice)
  if user_choice == cpu_choice:
    sleep(1)
    print "It's a tie."
  elif user_choice_index == 0 and cpu_choice_index == 2: #why index instead of direct referencing?
    sleep(1)
    print win
  elif user_choice_index == 1 and cpu_choice_index == 0:
    sleep(1)
    print win
  elif user_choice_index == 2 and cpu_choice_index == 1:
    sleep(1)
    print win
  elif user_choice_index > len(options)-1: #interesting add-on but it'll never happen?
    sleep(1)
    print "You have chosen an invalid option."
  else:
    sleep(1)
    print lose
  print
  return # <-- used when a function is ready to return a value to its caller

def play_RPS(): # where the user and computer actually make their choices
  print
  print "ROCK PAPER SCISSORS YO"
  print
  user_choice = raw_input("Select R for rock, P for paper, or S for scissors: ")
  user_choice = user_choice.upper()
  sleep(1)
  cpu_choice = options[randint(0,len(options)-1)]
  print
  decide_winner(user_choice, cpu_choice)

play_RPS()
