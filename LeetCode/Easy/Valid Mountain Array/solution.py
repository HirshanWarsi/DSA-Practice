class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        i = 0

        # Move uphill
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1

        # Check whether peak is at the beginning or end
        if i == 0 or i == n - 1:
            return False

        # Move downhill
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        return i == n - 1