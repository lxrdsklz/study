# выводит все гласные из слова 'Milliways'

vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'
for letter in word:
    if letter in vowels:
        print(letter)