# the challenge was Loops 19. "create your own loop using for & else, from scratch"
pokemon = ["pikachu", "snorlax", "meowth"]

print "You have caught"
for poke in pokemon:
    if poke == "charmander":
        print "oooh you have a charmander??"
        break
    print "a " + poke
else:
    print "you have caught them all * .05!"