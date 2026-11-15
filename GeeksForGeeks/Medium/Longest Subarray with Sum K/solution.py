class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum = 0
        max_length = 0
        hashmap = {0: -1}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            required = prefix_sum - k
            
            if required in hashmap:
                length = i - hashmap[required]
                max_length = max(max_length, length)
                
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i
                
        return max_length