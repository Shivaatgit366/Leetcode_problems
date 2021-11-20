# correct answer:-

user_string = "abca4567bdcaserw321q"
user_string2 = "abcdefserw3282346fgh"
user_string3 = "aaaaaaa"


def str_producer(str1):
    answers = []
    current_answer = ""
    for character in str1:
        if character not in current_answer:
            current_answer = current_answer + character
        else:
            answers.append(current_answer)
            index = current_answer.index(character)
            current_answer = current_answer[index + 1:]
            latest_answer = current_answer + character
    answers.append(current_answer)
    return answers

def max_len_item_finder(list1):
    max_len = len(list1[0])
    max_number_index = 0
    for index, item in enumerate(list1):
        if len(item) > max_len:
            max_len = len(item)
            max_number_index = index
    return max_len

print(str_producer(user_string))
print(max_len_item_finder(str_producer(user_string)))
print(str_producer(user_string2))
print(max_len_item_finder(str_producer(user_string2)))
print(str_producer(user_string3))