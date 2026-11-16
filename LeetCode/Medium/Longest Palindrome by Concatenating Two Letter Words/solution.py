class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        hashmap = {}

        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1

        length = 0
        middle = False

        for word in hashmap:
            reverse = word[::-1]

            if word[0] != word[1]:
                if reverse in hashmap:
                    pairs = min(hashmap[word], hashmap[reverse])
                    length += pairs * 4

                    hashmap[word] -= pairs
                    hashmap[reverse] -= pairs

            else:
                pairs = hashmap[word] // 2
                length += pairs * 4

                if hashmap[word] % 2 == 1:
                    middle = True

        if middle:
            length += 2

        return length