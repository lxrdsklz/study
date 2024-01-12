def search_for_vowels(phrase: str) -> set:
    """Выводит гласные, найденные в указанной фразе"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из 'letters', найденных в указанной фразе"""
    return set(letters).intersection(set(phrase))

