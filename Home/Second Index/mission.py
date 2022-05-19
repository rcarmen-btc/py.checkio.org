def second_index(text: str, symbol: str) -> [int, None]:
    """
		returns the second index of a symbol in a given text
	"""
    # your code here
    begin = 0
    n = 2
    while (n > 0):
        begin = text.find(symbol, begin, len(text))
        begin += 1 if (begin != -1) else 0
        n -= 1
    if (begin == -1):
        return (None)
    return begin - 1


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "a"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
