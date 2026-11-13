class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even_numbers = []
        odd_numbers = []

        for num in nums:
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)
                
        result = []

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even_numbers.pop())
            else:
                result.append(odd_numbers.pop())

        return result