class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        freq = {}

        for i in range(26):
            ch = chr(i + ord('a'))
            freq[ch] = widths[i]

        lines = 1
        wide = 0

        for ch in s:
            if wide + freq[ch] > 100:
                lines += 1
                wide = freq[ch]
            else:
                wide += freq[ch]

        return [lines, wide]