"""
Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, where the first m elements denote the
elements that should be merged, and the last n elements are set
to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        indx = m + n - 1

        if j < 0:
            return

        while indx >= 0:
            leftval = nums1[i] if i >= 0 else float("-inf")
            rightval = nums2[j] if j >= 0 else float("-inf")

            if leftval > rightval:
                nums1[indx] = leftval
                i -= 1
            else:
                nums1[indx] = rightval
                j -= 1

            indx -= 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    s.merge(nums1, 6, [1, 2, 2], 3)
    print(nums1)
    if nums1 == [-1, 0, 0, 1, 2, 2, 3, 3, 3]:
        print("Test case 1 passed")
