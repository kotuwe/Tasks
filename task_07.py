def combine_anagrams(words_array):
    low_words_array = [i.lower() for i in words_array]
    words_array2 = [[]]
    arg_i = low_words_array[0]
    while len(low_words_array) != 0:
        for i in low_words_array:
            if sorted(i) == sorted(arg_i) and i in low_words_array:
                words_array2[-1].append(i)
                low_words_array.remove(i)
            elif i == low_words_array[-1]:
                words_array2.append([])
                arg_i = low_words_array[0]
            else:
                continue

    return words_array2


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
                        "creams", "scream"]))
# # => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]
