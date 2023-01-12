import re


def count_words(string):
    frequency = {}
    string2 = re.findall(r'\b[a-z]{1,15}\b', string.lower())
    for word in string2:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    return frequency


print(count_words("A man, a plan, a canal -- Panama"))  # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo"))                  # => {"doo": 3, "bee": 2}