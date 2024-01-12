# выводит все гласные из набранного в консоли слова и исключает повторения, а также подсчитывает частоту

vowels = ['a', 'e', 'i', 'o', 'u']

word = input('Provide a word to search for vowels: ')

#word = 'Hitchhiker'
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)

found = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')


# for kv in sorted(found):
#     print(kv + ' was found ' + str(found[kv]) + ' time(s).')

# for k, v in sorted(found.items()):
#     print(k, ' was found', v, ' times(s)')


