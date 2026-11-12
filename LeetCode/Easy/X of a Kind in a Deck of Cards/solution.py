from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        freq = Counter(deck)
        common = 0

        for count in freq.values():
            common = gcd(common, count)
            
        return common >= 2