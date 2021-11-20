# find the longest palindromic substring.
# solution:-

# def palindrome_checker(stringg):  # gives boolean value True if the string is palindromic.
#     string1 = stringg.lower()
#     l = len(string1)
#     if l < 2:
#         return True
#     elif string1[0] == string1[l - 1]:
#         return palindrome_checker(string1[1:l - 1])
#     else:
#         return False

def palindrome_checker(stringg):  # gives boolean value True if the string is palindromic.
    string2 = stringg[::-1]
    if string2 == stringg:
        return True
    else:
        return False


def list_of_palindromic_substrings(abc):  # gives the list with substrings as its items.
    if palindrome_checker(abc):
        return [abc]
    elif len(abc) < 2:
        return [abc]
    else:
        substr = []
        for i in range(len(abc)):
            substr.append(abc[i])
            for j in range(i + 1, len(abc)):
                if palindrome_checker(abc[i:j + 1]):
                    substr.append(abc[i:j + 1])
    output = sorted(substr, key=lambda y: len(y))
    return output


def longest_palindromic_substring(s):
    list1 = list_of_palindromic_substrings(s)
    longest = list1[-1]
    return longest


if __name__ == '__main__':
    j = longest_palindromic_substring("SQQSYYSQQs")
    print(j)
    y = longest_palindromic_substring("babad")
    print(y)
    # """
    z = longest_palindromic_substring("ffffffffffffffffffffffffffffffffffffffff"
                                      "ffffffffffffffffffffffffffffffffffffffff"
                                      "ffffffffffffffffffffffffffffffffffffffff"
                                      "fffffffffffffffffffffffffffffffffffffff"
                                      "fffffffffffffffffffffffffffffffffffff"
                                      "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
                                      "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
                                      "fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
                                      "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
                                      "ffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggg"
                                      "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                                      "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                                      "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                                      "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                                      "ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                                      "gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
    # """
    print(z)
