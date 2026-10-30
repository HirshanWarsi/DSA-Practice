class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        freq = {}
        missing = -1
        repeated = -1

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in range(1, len(nums) + 1):
            if num not in freq:
                missing = num

            elif freq[num] > 1:
                repeated = num

        return [repeated, missing]