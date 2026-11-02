class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        freq = {0 : 1}
        count = 0
        
        for num in nums:
            if num % 2 != 0:
                prefix_sum += 1

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count