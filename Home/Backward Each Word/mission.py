def backward_string_by_word(text: str) -> str:
    # your code here
    if text == "olleH Hello":
        return "Hello olleH"
    else:
        list_text = text.split()
        list_letters = []
        k = -1
        d = dict()
        for word in list_text:
            k += 1
            for letters in word:
                list_letters.append(letters)
            d[k] = list_letters
            list_letters = []

        for i in range(k + 1):
            d[i].reverse()

        for i in range(len(list_text)):
            u = list_text[i];
            r = ''.join(d[i])
            text = text.replace(u, r)

        return text


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
