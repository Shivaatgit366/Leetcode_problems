# list1 = [3, 2, 100, 21, 18, 155]
# max = list1[0]
# maxvalue_index = 0
# for index, item in enumerate(list1):
#     if item > max:
#         max = item
#         maxvalue_index = index
# print(f"max value of {list1} is {max} and its index is {maxvalue_index}")
# ------------------------------------------------------------------------------------------------------------------
#
# list2 = ["ab", "chfhfg", "fhfyrh88", "reed", "gjg", "cnfh12", "ded"]
# list3 = []
# list4 = ["aaahdgdg"]
#
# def max_len_finder(list_item):
#     if len(list_item) == 0:
#         return f"empty list"
#     max_len = len(list_item[0])
#     max_len_item = list_item[0]
#     maxvalue_index = 0
#     for index, item in enumerate(list_item):
#         if len(item) > max_len:
#             max_len = len(item)
#             max_len_item = item
#             maxvalue_index = index
#     return f"{max_len_item} has maximum length {max_len} and it is at index {maxvalue_index}"
#
# print(max_len_finder(list3))