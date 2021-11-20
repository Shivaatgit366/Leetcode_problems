# In this example, we see how to put loop inside the loop and do iterations for the indexes.
# Remember:- We should not use enumerate function for iterations with indexes.


nums = [3, 2, 4]
target = 5

# def number_finding_list(nums, target):
#     i = 0
#     while i < len(nums):
#         a = nums[i]
#         j = 0
#         while j < len(nums):
#             b = nums[j]
#             if j > i:
#                 if a + b == target:
#                     return [a, b]
#             j = j + 1
#         i = i + 1


def number_finding_list2(nums, target):
    i = 0
    for a in nums:
        j = 0
        for b in nums:
            if j > i:
                if a + b == target:
                    return [a, b]
            j = j + 1
        i = i + 1

print(number_finding_list2(nums, target))