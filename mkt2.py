shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for x in food:
        if stock[x] > 0:
            total = prices[x] + total
            stock[x] = stock[x] - 1
    return total





# exercise from http://zetcode.com/lang/python/functions/

print
print
print

def showModuleName():
    print __doc__

def getModuleFile():
   return __file__

a = showModuleName()
b = getModuleFile()

print a, b

# another from above
def g():
    def f():
        print "f() function"
    f() # <-- wth, what is this? can't just define f(), need to execute it within g()

print "g() test"
g()