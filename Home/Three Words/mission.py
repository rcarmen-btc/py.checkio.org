def checkio(words: str) -> bool:
    words_list = words.split()
    words_in_succ = 0
    are_we_have_three_words = False
    for one_word in words_list:
        if one_word.isdigit() == False:
            words_in_succ += 1
            if words_in_succ >= 3:
                are_we_have_three_words = True
        else:
            words_in_succ = 0

    return are_we_have_three_words


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
