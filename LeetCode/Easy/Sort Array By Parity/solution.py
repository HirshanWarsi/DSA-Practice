class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even_numbers = []
        odd_numbers = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_numbers.append(nums[i])

            if nums[i] % 2 != 0:
                odd_numbers.append(nums[i])

        return even_numbers + odd_numbers