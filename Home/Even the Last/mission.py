def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0
    if (len(array) == 0):
        return 0
    for i in range(0, len(array), 2):
        sum += array[i]
    sum *= array[-1]
    print(sum)
    return sum


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
