# vowels = set('aeiou')
# word = input('Enter a word to search for vowels: ')
# found = vowels.intersection(set(word))
# for vowel in found:
#     print(vowel)

def search4vowels():
	vowels = set('aeiou')
	word = input('Enter a word to search for vowels: ')
	found = vowels.intersection(set(word))
	for vowel in found:
	    print(vowel)

