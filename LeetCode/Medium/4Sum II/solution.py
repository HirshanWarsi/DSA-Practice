class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hashmap = defaultdict(int)

        for n1 in nums1:
            for n2 in nums2:
                number_needed = -(n1 + n2)
                hashmap[number_needed] += 1

        number_of_tuples = 0
        for n3 in nums3:
            for n4 in nums4:
                number_of_tuples += hashmap[n3 + n4]

        return number_of_tuples