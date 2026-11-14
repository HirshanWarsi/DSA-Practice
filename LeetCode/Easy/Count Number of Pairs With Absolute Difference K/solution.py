class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pairs = 0

        for i in range(len(nums)):
            diff = 0
            for j in range(i + 1, len(nums)):
                diff = abs(nums[j] - nums[i])
                if diff == k:
                    pairs += 1

        return pairs