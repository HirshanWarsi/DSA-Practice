from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        license_freq = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        result = ""

        for word in words:
            word_freq = Counter(word.lower())

            if all(word_freq[ch] >= count for ch, count in license_freq.items()):
                if result == "" or len(word) < len(result):
                    result = word

        return result