def coincidence(list=None, range=None):
    if list is None or range is None:
        return []
    lst2 = []
    for i in list:
        if isinstance(i, int) and i in range:
            lst2.append(i)
        if isinstance(i, float):
            argument_i = int(i)
            if argument_i in range:
                lst2.append(i)
    return lst2


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))                       # => [3, 4, 5]
print(coincidence())                                                           # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))     # => [1, 2, 2.5]