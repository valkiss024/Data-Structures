import string


def find_missing_letter(lst):
    hash_map = {}

    for char in lst.lower():
        hash_map[char] = True

    for char in string.ascii_lowercase:
        if not hash_map.get(char, None):
            return char


print(find_missing_letter("The quick brown box jumps over a lazy dog"))
