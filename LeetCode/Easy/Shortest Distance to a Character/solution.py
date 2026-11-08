class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        result = []

        for i in range(len(s)):
            min_dist = float('inf')
            for j in range(len(s)):
                if s[j] == c:
                    distance = abs(i - j)
                    min_dist = min(min_dist, distance)
            result.append(min_dist)

        return result