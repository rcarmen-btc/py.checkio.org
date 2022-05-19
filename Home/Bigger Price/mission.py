def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code her
    max_price = -1
    max_index = 0
    top = []
    while (limit > 0):
        for i in range(len(data)):
            if (max_price < data[i]["price"] and data[i] not in top):
                max_index = i
                max_price = data[i]["price"]
            i += 1
        top.append(data[max_index])
        max_price = -1
        limit -= 1
    return top


if __name__ == '__main__':
    from pprint import pprint

    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
