def search4letters(phrase:str, letters:str="aeiou") -> set:
    return set(letters).intersection(set(phrase))
