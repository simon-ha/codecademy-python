'''This program will roll a pair of dice, and if user%'s guess is greater than the total value of the dice roll, the user wins.'''

from random import randint
from time import sleep

print "This is a dice game. Roll two die on your end, and then input the number. The assumption is that the game is using two 6-sided die. If you roll greater than the computer rolls, you win money and fame!"

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "this is higher than the max possible number!"
    return
  else:
    print "rollin'..."
    sleep(2)
    print "The first dice rolled %d" % first_roll
    sleep(1)
    print "..."
    sleep(1)
    print "The second dice rolled %d" %second_roll
    total_roll = first_roll + second_roll
    print "The total roll is %d" % total_roll
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "YOU WON!!!"
      return
    else:
      print "You lost, loser."
      return
    
roll_dice(6)
  