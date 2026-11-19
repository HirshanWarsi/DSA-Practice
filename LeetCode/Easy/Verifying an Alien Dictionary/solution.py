class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank = {}

        for i in range(len(order)):
            rank[order[i]] = i

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
                j += 1
            else:
                if len(w1) > len(w2):
                    return False

        return True