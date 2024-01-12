# выводит все гласные из набранного в консоли слова и исключает повторения

vowels = set('aeiou')
word = input('Provide a word to search for vowels: ')

vowels = set(vowels)
found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)
