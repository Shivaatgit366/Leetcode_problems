from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        latest_list = sorted(list_merger(nums1, nums2))
        return median_finder(latest_list)


def list_merger(nums1, nums2):
    latest_list = nums1 + nums2
    return latest_list


def median_finder(arr):
    if len(arr) % 2 != 0:
        median = arr[len(arr) // 2]
        return median
    else:
        list_output = [arr[(len(arr) // 2) - 1], arr[len(arr) // 2]]
        median = float(sum(list_output) / 2)
        return median


if __name__ == "__main__":
    nums1: List[int] = [10, 20, 30, 40]
    nums2: List[int] = [5, 6, 8, 10, 15]
    s = Solution()
    res2 = s.findMedianSortedArrays(nums1, nums2)
    print(res2)

    nums1: List[int] = [1, 20, 22, 40]
    nums2: List[int] = [5, 6, 8, 10, 30]
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)