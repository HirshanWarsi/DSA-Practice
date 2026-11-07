class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        hashmap = {}
        result = 0
        
        for i in range(len(arr)):
            if arr[i] not in hashmap:
                hashmap[arr[i]] = i
            else:
                result = max(result, i - hashmap[arr[i]])
                    
        return result