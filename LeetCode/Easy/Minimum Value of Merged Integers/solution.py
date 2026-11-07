class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        min_value = float('inf')

        for i in range(0, len(nums), 2):
            curr_value = int(str(nums[i]) + str(nums[i+1]))
            
            if curr_value < min_value:
                min_value = curr_value

        return min_value