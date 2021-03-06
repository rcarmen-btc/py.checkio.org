from pprint import pprint


def safe_pawns(pawns: set) -> int:
    alf = 'abcdefgh'
    abc = {c: i for i, c in enumerate(alf)}
    desk = [[0 for x in range(8)] for _ in range(8)]
    for pawn in pawns:
        x = abc[pawn[0]]
        y = int(pawn[1]) - 1
        desk[y][x] = 1
    all = 0
    for y, row in enumerate(desk):
        for x, col in enumerate(row):
            if col == 0:
                continue
            left_y, left_x = y + 1, x - 1
            right_y, right_x = y + 1, x + 1
            try:
                check_left = desk[left_y][left_x]
                if left_x == -1:
                    check_left = 0
                if check_left == 2:
                    check_left = 0
                if check_left == 1:
                    desk[left_y][left_x] = 2
            except:
                check_left = 0
            try:
                check_right = desk[right_y][right_x]
                if right_x == -1:
                    check_right = 0
                if check_right == 2:
                    check_right = 0
                if check_right == 1:
                    desk[right_y][right_x] = 2
            except:
                check_right = 0
            all += check_right + check_left
    return all


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
