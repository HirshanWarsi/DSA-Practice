class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        length = 1
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                length = 1
            
            max_length = max(max_length, length)

        return max_length