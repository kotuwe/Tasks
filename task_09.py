def connect_dicts(dict1, dict2):
    if sum(dict2.values()) >= sum(dict1.values()):
        dict3 = dict1 | dict2
    else:
        dict3 = dict2 | dict1

    for key, value in list(dict3.items()):
        if value < 10:
            del dict3[key]

    sorted_values = sorted(dict3.values())
    new_sorted_dictionary = {}
    for i in sorted_values:
        for k in dict3.keys():
            if dict3[k] == i:
                new_sorted_dictionary[k] = dict3[k]
                break
    return new_sorted_dictionary


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))                 # => {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))    # => {d: 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))               # => {"c": 11, "b": 12, "a": 15}
