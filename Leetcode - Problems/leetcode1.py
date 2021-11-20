# a function which gives numbers list, which adds up to the target.
def number_finding_list(nums, target):
    for index_a, a in enumerate(nums):
        for index_b, b in enumerate(nums):
            if index_b > index_a and (a + b) == target:
                return [a, b]

# a function to find out the indexes.
def index_list(nums, target):
    numberlist = number_finding_list(nums, target)
    for x in range(len(nums)):
        if nums[x] == numberlist[0]:
            index_a = x
            break
    for y in range(index_a + 1, len(nums)):
        if nums[y] == numberlist[1]:
            index_b = y
            break
    return [index_a, index_b]

def indexlist2(nums, target):
    for index_x, x in enumerate(nums):
        for index_y, y in enumerate(nums):
            if index_y > index_x and x + y == target:
                return [index_x, index_y]

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(index_list(nums, target))


# ---------------------------------------------------------------------------------------------------------------

"""
def two_sum(nums, target):
    for idx1, n in enumerate(nums):
        try:
            idx2 = nums.index(target - n)
            if idx2 != idx1:
                return [idx1, idx2]
        except ValueError:
            pass

print(two_sum(nums, target))
"""


"""
def addnumbers(nums, target):
    for i1,x in enumerate(nums):
        y = target - x
        if y in nums:
            i2 = nums.index(y)
            if i1 != i2:
                return [i1, i2]

print(addnumbers(nums, target))
"""