'''this is from codecademy, a program to translate your word into pyg latin'''

pyg = 'ay'

original = raw_input('Input a word:')

if len(original) > 0 and original.isalpha() and original[0] == 'q' or original[1] == 'h':
	word = original.lower()
	first = word[0] + word[1]
	new_word = word[2:len(word)] + first + pyg
	print new_word
elif len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word[1:len(word)] + first + pyg
	print new_word
else:
	print 'invalid'