"""This python program will enable you to ascertain the area of any type of geometric, two-dimensional, and closed shape"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "calculator booting up"

print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct unit"
option = raw_input("Enter C for Circle or T for Triangle: ")

option = option.upper()

if option == 'C':
  radius = float(raw_input("Input the radius: "))
  area = pi * radius**2
  print "the pie is baking..."
  sleep(1)
  print ("Area: %.2f. \n%s" %(area, hint))
elif option == 'T':
  base = float(raw_input("Input the base of the triangle: "))
  height = float(raw_input("Input the height of the triangle: "))
  area = 0.5*base*height
  print "Uni Bi Tri..."
  sleep(1)
  print ("Area: %.2f. \n%s" %(area, hint))
else:
  print "You have entered garbage. goodbye."
