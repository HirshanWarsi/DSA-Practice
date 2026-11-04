class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_num = max(nums)
        max_index = nums.index(max_num)

        for i, num in enumerate(nums):
            if i != max_index:
                if num * 2 > max_num:
                    return -1
        
        return max_index