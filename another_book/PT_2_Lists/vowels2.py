# выводит гласные и исключает повторения из слова 'Milliways'

vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)