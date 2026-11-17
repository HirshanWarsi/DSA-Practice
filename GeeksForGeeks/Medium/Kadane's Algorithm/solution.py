class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        prefix_sum = arr[0]
        max_sum = arr[0]
        
        for i in range(1, len(arr)):
            prefix_sum = max(arr[i], prefix_sum + arr[i])
            max_sum = max(max_sum, prefix_sum)
            
        return max_sum