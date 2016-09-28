#codecademy python - a day at the supermarket - 9. something of value
#challenge - how to do a sumproduct

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0
for x in prices:
    total = prices[x] * stock[x] + total #man i struggled with this line so hard
    #product = prices[x]*stock[x] <v alternative way to do it.
    #total = total + product
print total

