def search_for_vowels(word: str) -> set:
    """Выводит гласные, найденные в указанном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_for_letters(phrase: str, letters: str) -> set:
    """Выводит указанные буквы, которые встречаются в указанном слове"""
    return set(letters).intersection(set(phrase))