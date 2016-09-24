'''this is from codecademy, a program to translate your word into pyg latin'''

pyg = 'ay'

original = raw_input('Input a word:')

#this covers words that start with q or has an h as the letter (e.g., th-, sh-, wh-, etc.)
if len(original) > 0 and original.isalpha() and original[0] == 'q' or original[1] == 'h':
	#for 
	word = original.lower()
	first = word[0] + word[1]
	new_word = word[2:len(word)] + first + pyg
	print new_word
#this covers the rest of the words
elif len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word[1:len(word)] + first + pyg
	print new_word
#for any non-words, or blank entries
else:
	print 'invalid'