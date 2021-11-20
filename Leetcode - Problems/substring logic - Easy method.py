user_string = "abca4567abxcbdcaserw321q"

def earlier_method(s):
    res = []
    text = ""  # take a string, check whether the character is present inside the string, keep adding the characters.
    for i in s:
        if i not in text:
            text = text + i
        else:
            res.append(text)
            index = text.index(i)
            text = text[index + 1:] + i
    res.append(text)
    return res

print(earlier_method(user_string))