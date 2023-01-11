import re


def is_palindrome(string):
    if isinstance(string, int):
        string = str(string)
    if string is None:
        return False
    string = re.sub(r',|\s|:|\.|-|_|!|\'', '', string.lower())
    return list(string) == list(reversed(string))


print(is_palindrome("A man, a plan, a canal -- Panama"))    # => True
print(is_palindrome("Madam, I'm Adam!"))                        # => True
print(is_palindrome(333))                                                  # => True
print(is_palindrome(None))                                                # => False
print(is_palindrome("Abracadabra"))                                 # => False