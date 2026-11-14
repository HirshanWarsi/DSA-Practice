class Solution:
    def maxLength(self, arr):
        # code here
        n = len(arr)
        first_seen = {}
        max_length = 0
        prefix_sum = 0
        
        # Insert prefix sum 0 at index -1 to handle sum from start
        first_seen[0] = -1
        
        for i in range(n):
            prefix_sum += arr[i]

            if prefix_sum in first_seen:
                prev_index = first_seen[prefix_sum]
                length = i - prev_index
                max_length = max(max_length, length)
            else:
                first_seen[prefix_sum] = i
            
        return max_length