def sum_numbers(text: str) -> int:
    # your code heretext += ' '
    text += ' '
    abc1 = {"'", '"', '', ' ', 'e', 'g', 'k', 's', 'p', 'w', 'b', 'v', 'x', 'c', 'd', 'm', 'i', 'u', 'n', 'r', 'j', 'o',
            'y', 'f', 'l', 'a', 't', 'q', 'h', 'z'}
    abc2 = {'e', 'g', 'k', 's', 'p', 'w', 'b', 'v', 'x', 'c', 'd', 'm', 'i', 'u', 'n', 'r', 'j', 'o', 'y', 'f', 'l',
            'a', 't', 'q', 'h', 'z'}
    sum_in_txt = 0
    index = 0
    bigNums = ''
    for symbol in text:
        if symbol not in abc1 and text[index - 1] not in abc2 and text[index + 1] not in abc2:
            if text[index + 1] not in abc2:
                bigNums += symbol
            if text[index + 1] in abc1:
                sum_in_txt += int(bigNums)
                bigNums = ''
        index += 1
    return sum_in_txt


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
