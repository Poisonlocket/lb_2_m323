
def reverse_word(word1: str) -> str:
    return word1[::-1]


def palindrome_check(word1: str) -> bool:
    reverse = reverse_word(word1)
    if word1 == reverse:
        return True
    else:
        return False
