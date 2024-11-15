from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than n

        while k > 0:
            last = nums[-1]  # Save the last element
            # Shift all elements one position to the right
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            # Place the last element at the start
            nums[0] = last
            k -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]

    s.rotate(nums, 3)
    print(nums)