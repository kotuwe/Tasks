def max_odd(array):
    array2 = []
    try:
        for i in array:
            if (isinstance(i, int) or isinstance(i, float)) and i % 2 != 0:
                array2.append(i)
        array2 = int(max(array2))
        return array2
    except ValueError:
        return None


print(max_odd([1, 2, 3, 4, 4]))                               # => 3
print(max_odd([21.0, 2, 3, 4, 4]))                           # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))        # => 3
print(max_odd(['ololo', 'fufufu']))                        # => None
print(max_odd([2, 2, 4]))                                      # => None