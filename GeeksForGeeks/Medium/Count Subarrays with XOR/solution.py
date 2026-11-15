class Solution:
    def subarrayXor(self, arr, m):
        # code here
        count = 0
        hashmap = {}
        xor = 0
        
        for num in arr:
            xor ^= num
            count += hashmap.get(xor ^ m, 0)
            
            if xor == m:
                count += 1
                
            hashmap[xor] = hashmap.get(xor, 0) + 1
            
        return count