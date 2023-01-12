import math


def multiply_numbers(inputs=None):
    if inputs is None:
        return inputs
    if isinstance(inputs, float):
        inputs = str(inputs)
    inputs2 = []
    for i in inputs:
        if isinstance(i, int) or i.isdigit():
            inputs2.append(int(i))
        else:
            continue
    if not inputs2:
        return None
    return math.prod(inputs2)


print(multiply_numbers())                              # => None
print(multiply_numbers('ss'))                        # => None
print(multiply_numbers('1234'))                    # => 24
print(multiply_numbers('sssdd34'))               # => 12
print(multiply_numbers(2.3))                          # => 6
print(multiply_numbers([5, 6, 4]))                  # => 120
