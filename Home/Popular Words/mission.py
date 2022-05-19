def popular_words(text: str, words: list) -> dict:
    # your code here
    res = []
    count = 0
    text = text.strip('\n')
    text = text.lower()
    textArr = text.split()
    for w in words:
        for wo in textArr:
            if (wo == w):
                count += 1
        res.append(count)
        count = 0
    res = dict(zip(words, res))
    return res


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
