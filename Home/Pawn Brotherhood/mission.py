def safe_pawns(pawns: set) -> int:
    abc = 'abcdefghijklmnopqrstuvwxyz'
    num = '12345678'
    cnt = 0
    for pawn in pawns:
        letter_index = abc.index(pawn[0])
        number_of_pos = int(pawn[1])
        pre_lett = abc[letter_index - 1]
        after_lett = abc[letter_index + 1]
        after_pos = number_of_pos + 1
        pre_lett_pos = pre_lett + str(after_pos)
        after_lett_pos = after_lett + str(after_pos)
        for p in pawns:
            if p == pre_lett_pos:
                cnt += 1

    return cnt * 2


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
