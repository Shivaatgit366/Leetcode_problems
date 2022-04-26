"""

# Harry went for a tour to Indonesia which has lot of islands and these islands are connected by bridges.
# He wonders what will be the longest route connecting these islands.
# A list of hyphenated letters representing path between these islands are given.
# For ex:- "a-b" means a to b, "b-c" means path between b to c.
# No cycles exist in path of these islands, every island is connected to some other island.
# Help Harry to find the longest path that exist.
# input will be comma separated string, each string is a form of "a-b" type.

# "a-b", "b-c", "b-d" means there is a path from a to b(also b to a), b to c, and b to d.

# function should return longest path value as an integer.

# input: "a-b", "b-c", "b-d"
# output: 2
# explanation: path a-b-c or a-b-d


# solution:-

class Solution:
    def find_farthest_island(self, links: list[str]) -> int:
        list_of_strings = hyphenated_to_string(links)
        maximum = maximum_combinations(list_of_strings)
        return maximum


def hyphenated_to_string(links: list[str]) -> list[str]:
    list1 = []
    for item in links:
        x = item.replace("-", "")
        list1.append(x)
    return list1


def maximum_combinations(list1: list[str]) -> int:
    dict_of_strings = dict()
    required_string = ""
    for x in list1:
        for y in list1[1:]:
            if len(required_string) < 3:
                if x[0] or x[-1] in y:
                    if x != y and x[0] != y[0] and x[-1] != y[-1]:
                        required_string = x + y[-1]
            if len(required_string) >= 3:
                if x[0] or x[-1] in y:
                    if x[1:-1] not in y:
                        for item in y:
                            if item not in required_string:
                                required_string = required_string + item
        dict_of_strings[required_string] = len(required_string)

    final_dict = dict(sorted(dict_of_strings.items(), key=lambda kv: (kv[1], kv[0])))
    final_list_of_keys = list(final_dict.keys())
    return final_dict.get(final_list_of_keys[-1])


if __name__ == '__main__':
    test_object = Solution()
    print(test_object.find_farthest_island(["ab", "ac", "ad", "bd", "de", "ef", "af"]))

"""
# -------------------------------------------------------------------------------------------------

