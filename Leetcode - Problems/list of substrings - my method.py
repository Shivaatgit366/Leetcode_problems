# user_string = "abca4567abxcbdcaserw321q"
#
# def list_of_substrings(abc):  # gives the list with substrings as its items.
#     substr = []
#     for i in range(len(abc)):
#         for j in range(i+1, len(abc)):
#             if abc[i] != abc[j] and abc[i:j+1] not in substr and abc[j] not in abc[i:j]:
#                 substr.append(abc[i:j + 1])
#             elif abc[i] == abc[j]:
#                 break
#             elif abc[j] in abc[i:j]:
#                 break
#
#     output = sorted(substr, key=lambda y: len(y))
#     return output
#
# print(list_of_substrings(user_string))
# ---------------------------------------------------------------------------------------------------------------
