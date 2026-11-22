class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            number = num * num
            result.append(number)
            result.sort()

        return result