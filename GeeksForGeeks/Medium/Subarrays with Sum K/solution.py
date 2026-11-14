class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        n = len(arr)
        count = 0
        prefix_sum = 0
        freq = {0: 1}
        
        for num in arr:
            prefix_sum += num
            required = prefix_sum - k
            
            if required in freq:
                count += freq[required]
                
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
            
        return count