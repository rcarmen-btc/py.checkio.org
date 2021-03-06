def frequency_sort(items):
    # your code here
    if len(items) == len(set(items)):
        return items
    if len(items) == 0:
        return []
    items_list = list(dict.fromkeys(items))
    print(items_list)
    items_cnt = []
    for i in items_list:
        cnt = 0
        for k in range(len(items)):
            if i == items[k]:
                cnt += 1
        items_cnt.append(cnt)
    res = []
    while len(items_cnt) != 0:
        maximum = max(items_cnt)
        index = items_cnt.index(maximum)
        res += [items_list[index] for _ in range(maximum)]
        items_cnt.remove(items_cnt[index])
        items_list.remove(items_list[index])
    return res


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
